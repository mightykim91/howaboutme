from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=models.EmailField(unique=False)
    name = models.CharField(max_length=30)
    profile_saved = models.IntegerField(default=0)
    image_saved = models.IntegerField(default=0)
    similarity = models.IntegerField(default=0)

