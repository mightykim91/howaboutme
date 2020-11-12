from django.urls import path
from . import views

name = 'profiles'

urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('partners/', views.get_partners),
]