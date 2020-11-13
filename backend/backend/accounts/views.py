import requests
import json
import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from .serializers import UserSerializer
from .models import User

from profiles.serializers import ProfileListSerializer
from profiles.models import Profile
from preferences.serializers import PreferenceResponseSerializer
from preferences.models import Preference

URL = 'http://127.0.0.1:8000/'
FRONT_URL = 'http://localhost:8080/user/login'

# initial kakao login
def kakaoLogin(request):
    if not 'kakao_access_token' in request.session:
        with open('./secrets.json') as json_file:
            json_data = json.load(json_file)
            REST_API_KEY = json_data['KAKAO_API_KEY']
        REDIRECT_URI = FRONT_URL
        request_url = 'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={}&redirect_uri={}'.format(
            REST_API_KEY, REDIRECT_URI)
        msg = {
            'url': request_url
        }
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
    # 유저정보
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
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
        token_json = token.json()
        # print(token_json['user']['profile_saved'])
        profile = Profile.objects.filter(user=token_json['user']['id'])
        # profile = Profile.objects.all()
        # print(profile[0])
        if len(profile) == 1:
            serializer = ProfileListSerializer(profile[0])
            # print(dir(serializer))
            # print(serializer)
            token_json['profile'] = serializer.data
        # print(token_json)
        preference = Preference.objects.filter(user=token_json['user']['id'])
        # profile = Profile.objects.all()
        
        if len(preference) == 1:
            serializer = PreferenceResponseSerializer(preference[0])
            # print(dir(serializer))
            # print(serializer)
            token_json['preference'] = serializer.data
        # print(token_json)
        response = JsonResponse(token_json)
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

def googleLogin(request):
    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        REST_API_KEY = json_data['GOOGLE_CLIENT_ID']
    REDIRECT_URI = FRONT_URL
    request_url = "https://accounts.google.com/o/oauth2/v2/auth?client_id={}&redirect_uri={}&response_type=code&scope=email%20profile%20openid".format(
        REST_API_KEY, REDIRECT_URI)
    msg = {
        'url': request_url
    }
    return JsonResponse(msg, status=200)


@api_view(['post'])
def googleCallBack(request):
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(request.data['access_token'])
    }

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
        token_json = token.json()
        # print(token_json['user']['profile_saved'])
        profile = Profile.objects.filter(user=token_json['user']['id'])
        # profile = Profile.objects.all()
        # print(profile[0])
        if len(profile) == 1:
            serializer = ProfileListSerializer(profile[0])
            # print(dir(serializer))
            # print(serializer)
            token_json['profile'] = serializer.data
        # print(token_json)
        preference = Preference.objects.filter(user=token_json['user']['id'])
        # profile = Profile.objects.all()
        
        if len(preference) == 1:
            serializer = PreferenceResponseSerializer(preference[0])
            # print(dir(serializer))
            # print(serializer)
            token_json['preference'] = serializer.data
        # print(token_json)
        response = JsonResponse(token_json)
        # response = Response(serializer.data)
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

    REDIRECT_URI = FRONT_URL
    request_url = "https://nid.naver.com/oauth2.0/authorize?client_id={}&redirect_uri={}&response_type=token&state=howaboutme".format(
        REST_API_KEY, REDIRECT_URI)
    msg = {
        'url': request_url
    }
    return JsonResponse(msg, status=200)


@api_view(['post'])
def naverCallBack(request):
    # 유저정보
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(request.data['token'])
    }

    info_url = 'https://openapi.naver.com/v1/nid/me'
    user_info = requests.get(info_url, headers=headers).json()['response']
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
        body = {
            'username': user_info['name']+'naver',
            'password1': user_info['email'],
            'password2': user_info['email'],
        }
        token = requests.post(signup_url, data=body)
        user = get_object_or_404(User, username=user_info['name']+'naver')
        user.name = user_info['name']
        user.save()
        response = JsonResponse(token.json())
    return response



