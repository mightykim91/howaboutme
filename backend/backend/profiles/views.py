from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import ProfileSerializer
from .models import Profile, Body, Job, Education, Area, Religion

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.dict()
        body_pk = get_object_or_404(Body,name=request.data['body']).id
        data['body'] = body_pk
        job_pk = get_object_or_404(Job, name=request.data['job']).id
        data['job'] = job_pk
        education_pk = get_object_or_404(Education, name=request.data['education']).id
        data['education'] = education_pk
        area_pk = get_object_or_404(Area, name=request.data['area']).id
        data['area'] = area_pk
        religion_pk = get_object_or_404(Religion, name=request.data['religion']).id
        data['religion'] = religion_pk
        print(data)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            user = request.user
            user.profile_saved = 1
            user.save()
            return Response(serializer.data)
    
    def put(self,request):
        instance = get_object_or_404(Profile, user=request.user.id)
        try:
            data = request.data.dict()
            body_pk = get_object_or_404(Body,name=request.data['body']).id
            data['body'] = body_pk
            job_pk = get_object_or_404(Job, name=request.data['job']).id
            data['job'] = job_pk
            education_pk = get_object_or_404(Education, name=request.data['education']).id
            data['education'] = education_pk
            area_pk = get_object_or_404(Area, name=request.data['area']).id
            data['area'] = area_pk
            religion_pk = get_object_or_404(Religion, name=request.data['religion']).id
            data['religion'] = religion_pk
            serializer = ProfileSerializer(instance, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                msg = {
                    'msg':'success'
                }
                return JsonResponse(msg, status=200)
        except:
            msg = {
                'msg':'fail'
            }
            return JsonResponse(msg,status=500)