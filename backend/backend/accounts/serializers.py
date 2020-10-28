from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
