from firebase_admin import storage
from firebase_admin import credentials
import firebase_admin
import os
import shutil
from PIL import Image
import requests
import pyrebase


def search(dirname):
    filenames = os.listdir(dirname)
    folder_num = 1
    for i, filename in enumerate(filenames):
        print(i, filename)
        if i % 2000 == 0:
            folder_num += 1
        directory = 'img' + str(folder_num)
        if not os.path.exists(directory):
            os.makedirs(directory)
        full_name = os.path.join(dirname, filename)
        # print(full_name)
        im = Image.open(full_name)
        im.save(os.path.join(directory, filename))


# search('img/')


# cred = credentials.Certificate('serviceAccountKey.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'pillsogood-764c8.appspot.com'
# })

# bucket = storage.bucket()
# # print(bucket)

# image_data = requests.get(image_url).content
# blob = bucket.blob('new_cool_image.jpg')
# blob.upload_from_string(
#     image_data,
#     content_type='image/jpg'
# )
# print(blob.public_url)

config = {
    "apiKey": "AIzaSyDyvNcvx768p1qRiZTqsBPCy5slJrEeeZ0",
    "authDomain": "focused-zephyr-294413.firebaseapp.com",
    "databaseURL": "https://focused-zephyr-294413.firebaseio.com",
    "projectId": "focused-zephyr-294413",
    "storageBucket": "focused-zephyr-294413.appspot.com",
    "messagingSenderId": "785785164353",
    "appId": "1:785785164353:web:2a9d7735db304475efacc0",
    "measurementId": "G-XRXDNELPZS"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
# print(storage)


def put_image(dirname):
    filenames = os.listdir(dirname)
    # folder_num = 1
    for i, filename in enumerate(filenames):
        # print(i, filename)
        # if i % 2000 == 0:
        #     folder_num += 1
        # if i < 82800:
        #     continue
        # directory = 'img' + str(folder_num)
        # if not os.path.exists(directory):
        #     os.makedirs(directory)
        print(filename)
        full_name = os.path.join(dirname, filename)
        name = filename.split('.')
        if len(name[0]) == 0:
            continue
        print(full_name)
        storage.child(name[0]).put(full_name)
        print(i, "Image Uploaded")


put_image('dummy_images/')
