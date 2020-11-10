from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        user = request.user
        user.profile_saved = 1
        user.save()
        return Response(serializer.data)