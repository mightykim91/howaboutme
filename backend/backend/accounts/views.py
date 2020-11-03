import requests, json, os

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


URL = 'http://127.0.0.1:8000/'
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


#initial kakao login
def kakaoLogin(request):
    if not 'kakao_access_token' in request.session:
        with open('./secrets.json') as json_file:
            json_data = json.load(json_file)
            REST_API_KEY = json_data['KAKAO_API_KEY']
        REDIRECT_URI = f'{URL}accounts/login/kakao/callback/'
        request_url = 'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={}&redirect_uri={}'.format(REST_API_KEY, REDIRECT_URI)
    
        return redirect(request_url)
    else:
        msg = {
            'status': 'false',
            'error': '이미 로그인한 유저입니다.'
        }
        return JsonResponse(msg, status=401)


#kakao login redirect function
def kakaoCallBack(request):

    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        REST_API_KEY = json_data['KAKAO_API_KEY']

    code = request.GET.get('code', None)
    request_url = 'https://kauth.kakao.com/oauth/token'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'
    }
    body = {
        'grant_type':'authorization_code',
        'client_id': f'{REST_API_KEY}',
        'redirect_uri': f'{URL}accounts/login/kakao/callback/',
        'code': f'{code}',
    }
    token_response = requests.post(request_url, headers=headers, data=body)

    ##유저정보
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(token_response.json()['access_token'])
    }
    
    info_url = 'https://kapi.kakao.com/v2/user/me'
    user_info = requests.get(info_url, headers = headers).json()
    try:
        login_url = f'{URL}login/'
        user = get_object_or_404(User, username=user_info['kakao_account']['profile']['nickname']+'kakao')
        body = {
            'username':user_info['kakao_account']['profile']['nickname']+'kakao',
            'password':user_info['kakao_account']['email']
        }
        token = requests.post(login_url, data=body)
        response = JsonResponse(token.json())
    except:
        print('no')
        signup_url = f'{URL}signup/'
        body = {
            'username':user_info['kakao_account']['profile']['nickname']+'kakao',
            'password1':user_info['kakao_account']['email'],
            'password2':user_info['kakao_account']['email']
        }
        token = requests.post(signup_url, data=body)
        user = get_object_or_404(User, username=user_info['kakao_account']['profile']['nickname']+'kakao')
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
        'Authorization': f'Bearer {token}'
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

    REDIRECT_URI = f'{URL}accounts/login/google/callback/'
    request_url = "https://accounts.google.com/o/oauth2/v2/auth?client_id={}&redirect_uri={}&response_type=code&scope=email%20profile%20openid".format(REST_API_KEY, REDIRECT_URI)
    
    return redirect(request_url)
    
def googleCallBack(request):
    code = request.GET.get('code', None)

    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        REST_API_KEY = json_data['GOOGLE_CLIENT_ID']
        SECRET_KEY = json_data['GOOGLE_SECRET_KEY']

    request_url = 'https://www.googleapis.com/oauth2/v4/token'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded'
    }
    body = {
        'code':code,
        'client_id':REST_API_KEY,
        'client_secret':SECRET_KEY,
        'redirect_uri':f'{URL}accounts/login/google/callback/',
        'grant_type':'authorization_code'
    }
    token_response = requests.post(request_url,headers=headers,data=body)

    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(token_response.json()['access_token'])
    }
    
    info_url = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token={}'.format(token_response.json()['access_token'])
    user_info = requests.get(info_url).json()
    try:
        login_url = f'{URL}login/'
        user = get_object_or_404(User, username=user_info['name']+'google')
        body = {
            'username':user_info['name']+'google',
            'password':user_info['email']
        }
        token = requests.post(login_url, data=body)
        response = JsonResponse(token.json())
    except:
        print('no')
        signup_url = f'{URL}signup/'
        body = {
            'username':user_info['name']+'google',
            'password1':user_info['email'],
            'password2':user_info['email']
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

    REDIRECT_URI = f'{URL}accounts/login/naver/callback/'
    request_url = "https://nid.naver.com/oauth2.0/authorize?client_id={}&redirect_uri={}&response_type=code".format(REST_API_KEY, REDIRECT_URI)
    
    return redirect(request_url)

def naverCallBack(request):
    
    with open('./secrets.json') as json_file:
        json_data = json.load(json_file)
        REST_API_KEY = json_data['NAVER_CLIENT_ID']
        SECRET_KEY = json_data['NAVER_SECRET_KEY']

    code = request.GET.get('code', None)
    request_url = 'https://nid.naver.com/oauth2.0/token'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'
    }
    body = {
        'grant_type':'authorization_code',
        'client_id': REST_API_KEY,
        'client_secret': SECRET_KEY,
        'code':code,
    }
    token_response = requests.get(request_url, headers=headers, params=body)
    ##유저정보
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(token_response.json()['access_token'])
    }
    
    info_url = 'https://openapi.naver.com/v1/nid/me'
    user_info = requests.get(info_url, headers = headers).json()['response']
    # return JsonResponse(user_info)
    try:
        login_url = f'{URL}login/'
        user = get_object_or_404(User, username=user_info['name']+'naver')
        body = {
            'username':user_info['name']+'naver',
            'password':user_info['email']
        }
        token = requests.post(login_url, data=body)
        response = JsonResponse(token.json())
    except:
        print('no')
        signup_url = f'{URL}signup/'
        print(user_info)
        body = {
            'username':user_info['name']+'naver',
            'password1':user_info['email'],
            'password2':user_info['email'],
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
