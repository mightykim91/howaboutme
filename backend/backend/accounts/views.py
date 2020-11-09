import requests
import json
import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from firebase_admin import storage
import pyrebase

from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile

import mahotas as mh
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance
from PIL import Image
from glob import glob
import cv2 
import dlib

import tensorflow as tf
import tensorflow_hub as hub
import ssl

URL = 'http://127.0.0.1:8000/'
FRONT_URL = 'http://localhost:8080/user/login'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        user = request.user
        user.profile_saved = 1
        user.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dup_check(request):
    nick = request.data['nickname'].strip()
    profile = Profile.objects.filter(nickname=nick)

    if len(profile) == 0:
        return Response(status=200, data='true')
    else:
        return Response(status=401, data='false')


# initial kakao login
def kakaoLogin(request):
    if not 'kakao_access_token' in request.session:
        with open('./secrets.json') as json_file:
            json_data = json.load(json_file)
            REST_API_KEY = json_data['KAKAO_API_KEY']
        # REDIRECT_URI = '{}accounts/login/kakao/callback/'.format(URL)
        REDIRECT_URI = FRONT_URL
        request_url = 'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={}&redirect_uri={}'.format(
            REST_API_KEY, REDIRECT_URI)
        msg = {
            'url': request_url
        }
        # return redirect(request_url)
        return JsonResponse(msg, status=200)
    else:
        msg = {
            'status': 'false',
            'error': '이미 로그인한 유저입니다.'
        }
        return JsonResponse(msg, status=401)


# kakao login redirect function
@api_view(['post'])
def kakaoCallBack(request):

    # with open('./secrets.json') as json_file:
    #     json_data = json.load(json_file)
    #     REST_API_KEY = json_data['KAKAO_API_KEY']

    # code = request.GET.get('code', None)
    # request_url = 'https://kauth.kakao.com/oauth/token'
    # headers = {
    #     'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'
    # }
    # body = {
    #     'grant_type': 'authorization_code',
    #     'client_id': REST_API_KEY,
    #     'redirect_uri': '{}accounts/login/kakao/callback/'.format(URL),
    #     'code': code,
    # }
    # token_response = requests.post(request_url, headers=headers, data=body)

    # 유저정보
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        # 'Authorization': 'Bearer {}'.format(token_response.json()['access_token']),
        'Authorization': 'Bearer {}'.format(request.data['access_token']),
    }

    info_url = 'https://kapi.kakao.com/v2/user/me'
    user_info = requests.get(info_url, headers=headers).json()
    try:
        login_url = '{}login/'.format(URL)
        user = get_object_or_404(
            User, username=user_info['kakao_account']['profile']['nickname']+'kakao')
        body = {
            'username': user_info['kakao_account']['profile']['nickname']+'kakao',
            'password': user_info['kakao_account']['email']
        }
        token = requests.post(login_url, data=body)
        response = JsonResponse(token.json())
    except:
        signup_url = '{}signup/'.format(URL)
        body = {
            'username': user_info['kakao_account']['profile']['nickname']+'kakao',
            'password1': user_info['kakao_account']['email'],
            'password2': user_info['kakao_account']['email']
        }
        token = requests.post(signup_url, data=body)
        user = get_object_or_404(
            User, username=user_info['kakao_account']['profile']['nickname']+'kakao')
        user.name = user_info['kakao_account']['profile']['nickname']
        user.save()
        response = JsonResponse(token.json())
    return response


def kakaoLoginCheck(session):
    if 'kakao_access_token' in session:
        return True
    else:
        return False


def kakaoLogOut(request):
    headers = request.headers
    # if not 'access_token' in request.session:
    if not kakaoLoginCheck(request.session):
        msg = {
            'status': 'false',
            "error": '로그인 되어 있지 않은 유저입니다.'
        }
        return JsonResponse(msg, status=401)

    token = request.session['kakao_access_token']
    logout_url = 'https://kapi.kakao.com/v1/user/logout'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(logout_url, headers=headers)
    try:
        del request.session['kakao_access_token']
        request.session.flush()

    except KeyError:
        pass

    msg = {
        'status': 'true',
        'message': '로그아웃 되었습니다.'
    }

    return JsonResponse(msg, status=200)


def googleLogin(request):
    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        REST_API_KEY = json_data['GOOGLE_CLIENT_ID']

    # REDIRECT_URI = '{}accounts/login/google/callback/'.format(URL)
    REDIRECT_URI = 'http://localhost:8080/user/login'
    request_url = "https://accounts.google.com/o/oauth2/v2/auth?client_id={}&redirect_uri={}&response_type=code&scope=email%20profile%20openid".format(
        REST_API_KEY, REDIRECT_URI)
    msg = {
        'url': request_url
    }
    # return redirect(request_url)
    return JsonResponse(msg, status=200)


@api_view(['post'])
def googleCallBack(request):
    # print(request.data)
    # code = request.GET.get('code', None)
    # code = request.data['code']
    # print(code)
    # print('{}accounts/login/google/callback/'.format(URL))
    # with open('./secrets.json') as json_file:
    #     json_data = json.load(json_file)
    #     REST_API_KEY = json_data['GOOGLE_CLIENT_ID']
    #     SECRET_KEY = json_data['GOOGLE_SECRET_KEY']

    # request_url = 'https://www.googleapis.com/oauth2/v4/token'
    # headers = {
    #     'Content-type': 'application/x-www-form-urlencoded'
    # }
    # body = {
    #     'code': code,
    #     'client_id': REST_API_KEY,
    #     'client_secret': SECRET_KEY,
    #     'redirect_uri': '{}accounts/login/google/callback/'.format(URL),
    #     'grant_type': 'authorization_code'
    # }
    # token_response = requests.post(request_url, headers=headers, data=body)
    # print(token_response.json())
    print(request.data)
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        # 'Authorization': 'Bearer {}'.format(token_response.json()['access_token']),
        'Authorization': 'Bearer {}'.format(request.data['access_token'])
    }

    # info_url = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token={}'.format(
    #     token_response.json()['access_token'])
    info_url = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token={}'.format(
        request.data['access_token'])
    user_info = requests.get(info_url).json()
    try:
        login_url = '{}login/'.format(URL)
        user = get_object_or_404(User, username=user_info['name']+'google')
        body = {
            'username': user_info['name']+'google',
            'password': user_info['email']
        }
        token = requests.post(login_url, data=body)
        response = JsonResponse(token.json())
    except:
        signup_url = '{}signup/'.format(URL)
        body = {
            'username': user_info['name']+'google',
            'password1': user_info['email'],
            'password2': user_info['email']
        }
        token = requests.post(signup_url, data=body)
        user = get_object_or_404(User, username=user_info['name']+'google')
        user.name = user_info['name']
        user.save()
        response = JsonResponse(token.json())
    return response


def naverLogin(request):
    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        REST_API_KEY = json_data['NAVER_CLIENT_ID']

    # REDIRECT_URI = '{}accounts/login/naver/callback/'.format(URL)
    REDIRECT_URI = 'http://localhost:8080/user/login'
    request_url = "https://nid.naver.com/oauth2.0/authorize?client_id={}&redirect_uri={}&response_type=token&state=howaboutme".format(
        REST_API_KEY, REDIRECT_URI)
    msg = {
        'url': request_url
    }
    # return redirect(request_url)
    return JsonResponse(msg, status=200)


@api_view(['post'])
def naverCallBack(request):

    # with open('./secrets.json') as json_file:
    #     json_data = json.load(json_file)
    #     REST_API_KEY = json_data['NAVER_CLIENT_ID']
    #     SECRET_KEY = json_data['NAVER_SECRET_KEY']

    # code = request.GET.get('code', None)
    # request_url = 'https://nid.naver.com/oauth2.0/token'
    # headers = {
    #     'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    # }
    # body = {
    #     'grant_type': 'authorization_code',
    #     'client_id': REST_API_KEY,
    #     'client_secret': SECRET_KEY,
    #     'code': code,
    # }
    # token_response = requests.get(request_url, headers=headers, params=body)
    # 유저정보
    print(request.data)
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        # 'Authorization': 'Bearer {}'.format(token_response.json()['access_token']),
        'Authorization': 'Bearer {}'.format(request.data['token'])
    }

    info_url = 'https://openapi.naver.com/v1/nid/me'
    user_info = requests.get(info_url, headers=headers).json()['response']
    # return JsonResponse(user_info)
    try:
        login_url = '{}login/'.format(URL)
        user = get_object_or_404(User, username=user_info['name']+'naver')
        body = {
            'username': user_info['name']+'naver',
            'password': user_info['email']
        }
        token = requests.post(login_url, data=body)
        response = JsonResponse(token.json())
    except:
        signup_url = '{}signup/'.format(URL)
        print(user_info)
        body = {
            'username': user_info['name']+'naver',
            'password1': user_info['email'],
            'password2': user_info['email'],
        }
        print(body)
        token = requests.post(signup_url, data=body)
        user = get_object_or_404(User, username=user_info['name']+'naver')
        user.name = user_info['name']
        user.save()
        response = JsonResponse(token.json())
    return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def imageUpload(request):
    try:
        with open('./secrets.json') as json_file:
            json_data = json.load(json_file)
            firebaseConfig = json_data['FIREBASE_CONFIG']
        firebase = pyrebase.initialize_app(firebaseConfig)
        storage = firebase.storage()
        print(request.user.profile.nickname)
        image_file = request.FILES['image']
        storage.child(request.user.profile.nickname).put(image_file)
        msg = {
            'status': 'true',
            'message': '이미지가 성공적으로 저장되었습니다.'
        }

        return JsonResponse(msg, status=200)
    except:
        msg = {
            'status': 'false',
            'message': '이미지 저장에 실패했습니다.'
        }

        return JsonResponse(msg, status=500)

def chist(im):
    im = im//64
    r, g, b = im.transpose( (2, 0, 1) )
    pixels = 1*r + 4*g + 16*b
    hist = np.bincount(pixels.ravel(), minlength=64)
    hist = hist.astype(float)
    return np.log1p(hist)

# @api_view(['post'])
# def imageAnalysis(request):
#     im1 = Image.open(request.FILES['image1'])
#     im2 = Image.open(request.FILES['image2'])
#     # print(im1)
#     # print(im2)
#     im1.save('image1.jpg')
#     im2.save('image2.jpg')
    
#     images = glob('./image*.jpg')
#     for i, im in enumerate(images):
#         # if i == 1:
#         #     break
#         face_detector = dlib.get_frontal_face_detector()
#         img = cv2.imread(im)
#         faces = face_detector(img)

#         print("{} faces are detected".format(len(faces)))
#         crop = img[faces[0].top():faces[0].bottom(), faces[0].left():faces[0].right()]
#         cv2.imwrite(im, crop)
#     # print(images)
#     features = []
#     for im in images:
#         imcolor = mh.imread(im)
#         im = mh.colors.rgb2gray(imcolor, dtype=np.uint8)
#         features.append(np.concatenate([mh.features.haralick(im).ravel(), chist(imcolor)]))
#     sc = StandardScaler()
#     features = sc.fit_transform(features)

#     dists = distance.squareform(distance.pdist(features))
#     print(dists)
#     print(dists[0][1])
    # os.remove('./image1.jpg')
    # os.remove('./image2.jpg')

CHANNELS = 3
def build_graph(hub_module_url, target_image_path):
    ssl._create_default_https_context = ssl._create_unverified_context

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
    try:
        im1 = Image.open(request.FILES['image1'])
        im2 = Image.open(request.FILES['image2'])
        # print(im1)
        # print(im2)
        im1.save('target_image.jpg')
        im2.save('compare_image.jpg')
        images = glob('./*.jpg')
        for i, im in enumerate(images):
            face_detector = dlib.get_frontal_face_detector()
            img = cv2.imread(im)
            faces = face_detector(img)

            print("{} faces are detected".format(len(faces)))
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

        print(similarities[1])
        similar = round(similarities[1]*100) 
        msg = {
            'msg':'success',
            'similarity':str(similar)
        }
        os.remove('./target_image.jpg')
        os.remove('./compare_image.jpg')
        return JsonResponse(msg, status=200)
    except:
        msg = {
            'msg':'fail'
        }
        return JsonResponse(msg, status=500)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def imageSimilarity(request):
    try:
        print(request.data['similarity'])
        user = request.user
        user.similarity = request.data['similarity']
        user.save()
        msg = {
            'msg':'success'
        }
        return JsonResponse(msg, status=200)
    except:
        msg = {
            'msg':'fail'
        }
        return JsonResponse(msg, status=500)
