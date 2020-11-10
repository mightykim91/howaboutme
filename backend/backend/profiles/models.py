from django.db import models
from accounts.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=10)
    gender = models.IntegerField()
    birth = models.DateField()
    height = models.FloatField()
    body = models.CharField(max_length=50)
    hobby1 = models.CharField(max_length=50)
    hobby2 = models.CharField(max_length=50)
    blood = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    smoke = models.CharField(max_length=50)
    drink = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    area = models.CharField(max_length=20)
    intro = models.CharField(max_length=150)