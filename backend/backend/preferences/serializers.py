from rest_framework import serializers

from profiles.models import Body, Education, Job, Area, Religion
from profiles.serializers import AreaSerializer, EducationSerializer, JobSerializer, BodySerializer, ReligionSerializer
from .models import Preference
from accounts.serializers import UserSerializer

class PreferenceResponseSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    area = AreaSerializer(many=True, required=False)
    education = EducationSerializer(many=True, required=False)
    job = JobSerializer(many=True, required=False)
    religion = ReligionSerializer(many=True, required=False)
    body = BodySerializer(many=True, required=False)
    class Meta:
        model = Preference
        fields = '__all__'

class PreferenceSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Preference
        fields = '__all__'