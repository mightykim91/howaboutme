from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dup_check(request):
    nick = request.data['nickname'].strip()
    profile = Profile.objects.filter(nickname=nick)

    if len(profile) == 0:
        return Response(status=200, data='true')
    else:
        return Response(status=401, data='false')
