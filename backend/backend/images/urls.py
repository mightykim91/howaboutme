from django.urls import path
from . import views

name = 'images'

urlpatterns = [
    path('analysis/', views.imageAnalysis),
    path('upload/', views.imageUpload),
    path('similarity/', views.imageSimilarity),
]