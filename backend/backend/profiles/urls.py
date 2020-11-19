from django.urls import path
from . import views

name = 'profiles'

urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('<int:user_id>/', views.get_profile),
    path('partners/', views.get_partners),
]