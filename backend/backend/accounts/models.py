from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_saved = models.IntegerField(default=0)
    image_saved = models.IntegerField(default=0)
    similarity = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    gender = models.IntegerField(max_length=1)
    birth = models.DateField()
    height = models.FloatField()
    body = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    blood = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    smoke = models.CharField(max_length=50)
    drink = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
