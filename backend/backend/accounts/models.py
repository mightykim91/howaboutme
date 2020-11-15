from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email=models.EmailField(unique=False)
    name = models.CharField(max_length=150)
    profile_saved = models.IntegerField(default=0)
    image_saved = models.IntegerField(default=0)
    similarity = models.IntegerField(default=0)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked')
