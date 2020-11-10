from django.db import models
from accounts.models import User
import datetime

class Body(models.Model):
    name = models.CharField(max_length=10)

class Education(models.Model):
    name = models.CharField(max_length=20)

class Job(models.Model):
    name = models.CharField(max_length=20)

class Religion(models.Model):
    name = models.CharField(max_length=10)

class Area(models.Model):
    name = models.CharField(max_length=20)

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
    religion = models.OneToOneField(Religion, on_delete=models.CASCADE)
    smoke = models.CharField(max_length=50)
    drink = models.CharField(max_length=50)
    education = models.OneToOneField(Body, on_delete=models.CASCADE)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    area = models.OneToOneField(Area, on_delete=models.CASCADE)
    intro = models.CharField(max_length=150)
    age = models.IntegerField(default=0)

    def set_age(self):
        my_age = int((datetime.date.today() - self.birth).days//365)+1
        self.age = my_age

    def save(self, *args, **kwargs):
        self.set_age()
        super(Profile,self).save(*args,**kwargs)