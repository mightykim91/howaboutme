from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path('profile/', views.set_profile),
    path('nick-dup-check/', views.dup_check),
    path('login/kakao/', views.kakaoLogin),
    path('login/kakao/callback/', views.kakaoCallBack),
    path('logout/kakao/', views.kakaoLogOut),
]
