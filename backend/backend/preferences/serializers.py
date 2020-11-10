from rest_framework import serializers

from profiles.models import Body, Education, Job, Area, Religion
from .models import Preference
from accounts.serializers import UserSerializer

class PreferenceSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    
    class Meta:
        model = Preference
        fields = '__all__'