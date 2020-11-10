from django.urls import path
from . import views

name = 'preferences'

urlpatterns = [
    path('', views.PreferenceView.as_view())
]