from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# image similarity
from PIL import Image
from glob import glob
import cv2 
import dlib
import tensorflow as tf
import tensorflow_hub as hub
import os

# image upload
from firebase_admin import storage
import pyrebase
import json

CHANNELS = 3
def build_graph(hub_module_url, target_image_path):
    module = hub.Module('./imagenet_mobilenet_v2_100_96_feature_vector_1')
    height, width = hub.get_expected_image_size(module)

    def decode_and_resize(image_str_tensor):
        image = tf.image.decode_image(image_str_tensor, channels=CHANNELS)

        image = tf.expand_dims(image,0)
        image = tf.compat.v1.image.resize_bilinear(
            image, [height,width], align_corners=False
        )

        image = tf.compat.v1.squeeze(image, squeeze_dims=[0])
        image = tf.cast(image, dtype=tf.uint8)
        return image
    
    def to_img_feature(images):
        outputs = module(dict(images=images), signature="image_feature_vector", as_dict=True)
        return outputs['default']
    
    target_image_bytes = tf.io.gfile.GFile(target_image_path, 'rb').read()
    target_image = tf.constant(target_image_bytes, dtype=tf.string)
    target_image = decode_and_resize(target_image)
    target_image = tf.image.convert_image_dtype(target_image, dtype=tf.float32)
    target_image = tf.expand_dims(target_image, 0)
    target_image = to_img_feature(target_image)

    input_byte = tf.compat.v1.placeholder(tf.string, shape=[None])
    input_image = tf.map_fn(decode_and_resize, input_byte, back_prop=False, dtype=tf.uint8)
    input_image = tf.image.convert_image_dtype(input_image, dtype=tf.float32)
    input_image = to_img_feature(input_image)

    dot = tf.tensordot(target_image, tf.transpose(input_image), 1)
    similarity = dot / (tf.norm(target_image, axis=1)*tf.norm(input_image, axis=1))
    similarity = tf.reshape(similarity, [-1])

    return input_byte, similarity

@api_view(['post'])
@permission_classes([IsAuthenticated])
def imageAnalysis(request):
    # try:
    im1 = Image.open(request.FILES['image1'])
    im2 = Image.open(request.FILES['image2'])
    print(im1)
    print(im2)
    im1.save('target_image.jpeg')
    im2.save('compare_image.jpeg')
    images = glob('./*.jpeg')
    print(images)
    for i, im in enumerate(images):
        face_detector = dlib.get_frontal_face_detector()
        img = cv2.imread(im)
        faces = face_detector(img)
        print(len(faces),'face cropped')
        crop = img[faces[0].top():faces[0].bottom(), faces[0].left():faces[0].right()]
        cv2.imwrite(im, crop)
    image_bytes = []
    image_bytes.append(tf.io.gfile.GFile('target_image.jpg','rb').read())
    image_bytes.append(tf.io.gfile.GFile('compare_image.jpg','rb').read())
    hub_module_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/4" #@param {type:"string"}
    with tf.Graph().as_default():
        input_byte, similarity_op = build_graph(hub_module_url, 'target_image.jpg')

        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())

            similarities = sess.run(similarity_op, feed_dict = {input_byte: image_bytes})
            
    similar = round(similarities[1]*100)
    msg = {
        'msg':'success',
        'similarity':str(similar)
    }
    os.remove('./target_image.jpg')
    os.remove('./compare_image.jpg')
    return JsonResponse(msg, status=200)
    # except:
    #     msg = {
    #         'msg':'fail'
    #     }
    #     return JsonResponse(msg, status=500)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def imageSimilarity(request):
    # try:
    user = request.user
    user.similarity = request.data['similarity']
    user.image_saved = 1
    user.save()
    msg = {
        'similarity':request.data['similarity']
    }
    return JsonResponse(msg, status=200)
    # except:
    #     msg = {
    #         'msg':'fail'
    #     }
    #     return JsonResponse(msg, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def imageUpload(request):
    # try:
    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        firebaseConfig = json_data['FIREBASE_CONFIG']
    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()
    image_file = request.FILES['image']
    storage.child(request.user.profile.nickname).put(image_file)
    msg = {
        'status': 'true',
        'message': '이미지가 성공적으로 저장되었습니다.'
    }

    return JsonResponse(msg, status=200)
    # except:
    #     msg = {
    #         'status': 'false',
    #         'message': '이미지 저장에 실패했습니다.'
    #     }

    #     return JsonResponse(msg, status=500)
