from django.db import models
from accounts.models import User
from profiles.models import Body,Education,Job,Religion,Area

class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preference')
    area = models.ManyToManyField(
        Area, related_name='preference'
    )
    min_age = models.IntegerField(default=20)
    max_age = models.IntegerField(default=50)
    min_height = models.IntegerField(default=140)
    max_height = models.IntegerField(default=200)
    drink = models.CharField(max_length=10)
    smoke = models.CharField(max_length=10)
    body = models.ManyToManyField(
        Body, related_name='preference'
    )
    education = models.ManyToManyField(
        Education, related_name='preference'
    )
    job = models.ManyToManyField(
        Job, related_name='preference'
    )
    religion = models.ManyToManyField(
        Religion, related_name='preference'
    )

