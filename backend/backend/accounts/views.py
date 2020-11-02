import requests, json, os

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
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
    if not 'access_token' in request.session:
        with open('./secrets.json') as json_file:
            json_data = json.load(json_file)
            REST_API_KEY = json_data['KAKAO_API_KEY']
        REDIRECT_URI = 'http://127.0.0.1:8000/accounts/login/kakao/callback/'
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
        'redirect_uri': 'http://127.0.0.1:8000/accounts/login/kakao/callback/',
        'code': f'{code}',
    }
    token_response = requests.post(request_url, headers=headers, data=body)

    ##유저정보
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': 'Bearer {}'.format(token_response.json()['access_token'])
    }
    
    info_url = 'https://kapi.kakao.com/v2/user/me'
    user_info = requests.get(info_url, headers = headers)
    response = JsonResponse(user_info.json())
    access_token = token_response.json()['access_token']
    request.session['access_token'] = access_token
    return response


def kakaoLoginCheck(session):
    if 'access_token' in session:
        return True
    else:
        return False


def kakaoLogOut(request):
    headers = request.headers
    if not 'access_token' in request.session:
        msg = {
            'status': 'false',
            "error": '로그인 되어 있지 않은 유저입니다.'
        }
        return JsonResponse(msg, status=401)
    
    token = request.session['access_token']
    logout_url = 'https://kapi.kakao.com/v1/user/logout'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(logout_url, headers=headers)
    try:
        del request.session['access_token']
        request.session.flush()
        
    except KeyError:
        pass
    
    msg = {
        'status': 'true',
        'message': '로그아웃 되었습니다.'
    }
    
    return JsonResponse(msg, status=200)
    
    
    
    
    
    
       
