from django.urls import path
from . import views

name = 'profiles'

urlpatterns = [
    path('', views.set_profile),
]