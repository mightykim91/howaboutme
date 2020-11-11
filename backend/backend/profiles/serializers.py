from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        exclude = ['age']
