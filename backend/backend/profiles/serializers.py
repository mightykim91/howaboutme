from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Profile, Body, Job, Religion, Education, Area

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    birth = serializers.DateField(format="%Y-%m-%d")
    like = serializers.BooleanField(required=False)
    class Meta:
        model = Profile
        exclude = ['age']

class ProfileListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    body = BodySerializer()
    job = JobSerializer()
    area = AreaSerializer()
    education = EducationSerializer()
    like = serializers.BooleanField(required=False)

    class Meta:
        model=Profile
        fields = '__all__'