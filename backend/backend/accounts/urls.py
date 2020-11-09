from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path('profile/', views.set_profile),
    path('nick-dup-check/', views.dup_check),
    path('login/kakao/', views.kakaoLogin),
    path('login/kakao/callback/', views.kakaoCallBack),
    path('logout/kakao/', views.kakaoLogOut),
    path('login/google/', views.googleLogin),
    path('login/google/callback/', views.googleCallBack),
    path('login/naver/', views.naverLogin),
    path('login/naver/callback/', views.naverCallBack),
    path('image/upload/', views.imageUpload),
    path('image/analysis/', views.imageAnalysis),
    path('image/similarity/', views.imageSimilarity),
]
