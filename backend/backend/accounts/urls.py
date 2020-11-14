from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path('login/kakao/', views.kakaoLogin),
    path('login/kakao/callback/', views.kakaoCallBack),
    path('login/google/', views.googleLogin),
    path('login/google/callback/', views.googleCallBack),
    path('login/naver/', views.naverLogin),
    path('login/naver/callback/', views.naverCallBack),
    path('like/', views.like),
]
