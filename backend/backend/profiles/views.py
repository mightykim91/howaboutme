from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q,F
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import ProfileSerializer, ProfileListSerializer
from .models import Profile, Body, Job, Education, Area, Religion
from preferences.models import Preference
from preferences.serializers import PreferenceSerializer
from accounts.models import User

import random


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        data = ProfileListSerializer(profile).data
        data['body'] = data['body']['name']
        data['job'] = data['job']['name']
        data['education'] = data['education']['name']
        data['area'] = data['area']['name']
        data['religion'] = data['religion']['name']
        if data['gender'] == 0:
            data['gender'] = '여자'
        else:
            data['gender'] = '남자'
        print(data)
        return Response(data)


    def post(self, request):
        data = request.data
        print(data)
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
        if data['gender'] == '여자':
            data['gender'] = 0
        else:
            data['gender'] = 1

        serializer = ProfileSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            user = request.user
            user.profile_saved = 1
            user.save()
            profile = get_object_or_404(Profile, user=request.user)
            data = ProfileListSerializer(profile).data
            data['body'] = data['body']['name']
            data['job'] = data['job']['name']
            data['education'] = data['education']['name']
            data['area'] = data['area']['name']
            data['religion'] = data['religion']['name']
            print(data)
            return Response(data)
    
    def put(self,request):
        instance = get_object_or_404(Profile, user=request.user.id)
        # try:    
        data = request.data
        print(data)
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
        if data['gender'] == '여자':
            data['gender'] = 0
        else:
            data['gender'] = 1
        serializer = ProfileSerializer(instance, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            msg = {
                'msg':'success'
            }
            return JsonResponse(msg, status=200)
        # except:
            # msg = {
            #     'msg':'fail'
            # }
            # return JsonResponse(msg,status=500)
    
    def delete(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        profile.delete()
        return JsonResponse({'msg':'success delete'}, status=200)

@api_view(['get'])
@permission_classes([IsAuthenticated])
def get_profile(request, user_id):
    profile = get_object_or_404(Profile, user=user_id)
    serializer = ProfileListSerializer(profile)
    return Response(serializer.data)
    
@api_view(['get'])
@permission_classes([IsAuthenticated])
def get_partners(request):
    gender = (request.user.profile.gender+1)%2
    # print(gender)
    like_users = request.user.like.all().values('id')
    # print(like_users)
    preference = Preference.objects.filter(user=request.user)
    all_profiles = Profile.objects.filter(gender=gender)
    print(len(preference))
    active_users = User.objects.filter(image_saved=1)
    if len(preference) == 0 or len(all_profiles) < 5:
        profiles = list(Profile.objects.filter(Q(gender=gender)&Q(user__in=active_users)))
        random.shuffle(profiles)
        profiles = profiles[:5]
        # print(type(profiles[0]))
        data = []
        for profile in profiles:
            # print(profile)
            serializer = ProfileListSerializer(profile).data
            # print(dir(serializer))
            flag = False
            for like_id in like_users:
                if like_id['id'] == profile.user.id:
                    flag = True
                    break
    
            if flag:
                serializer['like'] = True
                # data.append(ProfileListSerializer(data=profile, like=True))
            else:
                # data.append(ProfileListSerializer(data=profile, like=False))
                serializer['like'] = False
            # print(serializer)
            data.append(serializer)

        # print(data)
        # return Response(data)
        # serializer = ProfileListSerializer(data=data, many=True)
        # if serializer.is_valid(raise_exception=True):

        #     return Response(serializer.data)
        return Response(data)
    else:
        serializer = PreferenceSerializer(preference[0])
        # print(dir(serializer.data))
        # print(serializer.data)
        # print(len(preference[0].drink))
        # print(preference[0].drink == "상관 없음")
        if preference[0].drink == "상관 없음":
            if preference[0].smoke == "상관 없음":
                print(1)
                profiles = Profile.objects.filter(
                    Q(age__range=(preference[0].min_age,preference[0].max_age))
                    &Q(height__range=(preference[0].min_height,preference[0].max_height))
                    &Q(area__in=serializer.data['area'])&Q(body__in=serializer.data['body'])
                    &Q(education__in=serializer.data['education'])&Q(job__in=serializer.data['job'])
                    &Q(religion__in=serializer.data['religion'])&Q(gender=gender)
                    &Q(user__in=active_users)
                )
            else:
                print(2)
                profiles = Profile.objects.filter(
                    Q(age__range=(preference[0].min_age,preference[0].max_age))
                    &Q(height__range=(preference[0].min_height,preference[0].max_height))
                    &Q(smoke__startswith=preference[0].smoke)
                    &Q(area__in=serializer.data['area'])&Q(body__in=serializer.data['body'])
                    &Q(education__in=serializer.data['education'])&Q(job__in=serializer.data['job'])
                    &Q(religion__in=serializer.data['religion'])&Q(gender=gender)
                    &Q(user__in=active_users)
                )
        else:
            if preference[0].smoke == "상관 없음":
                print(3)
                profiles = Profile.objects.filter(
                    Q(age__range=(preference[0].min_age,preference[0].max_age))
                    &Q(height__range=(preference[0].min_height,preference[0].max_height))
                    &Q(drink__startswith=preference[0].drink)
                    &Q(area__in=serializer.data['area'])&Q(body__in=serializer.data['body'])
                    &Q(education__in=serializer.data['education'])&Q(job__in=serializer.data['job'])
                    &Q(religion__in=serializer.data['religion'])&Q(gender=gender)
                    &Q(user__in=active_users)
                )
            else:
                print(4)
                profiles = Profile.objects.filter(
                    Q(age__range=(preference[0].min_age,preference[0].max_age))
                    &Q(height__range=(preference[0].min_height,preference[0].max_height))
                    &Q(drink__startswith=preference[0].drink)&Q(smoke__startswith=preference[0].smoke)
                    &Q(area__in=serializer.data['area'])&Q(body__in=serializer.data['body'])
                    &Q(education__in=serializer.data['education'])&Q(job__in=serializer.data['job'])
                    &Q(religion__in=serializer.data['religion'])&Q(gender=gender)
                    &Q(user__in=active_users)
                )
        # print(profiles)
        profiles = list(profiles)
        while len(profiles) < 5:
            extra_profiles = list(Profile.objects.all())
            random.shuffle(extra_profiles)
            last_profile = extra_profiles[0]
            for p in profiles:
                if last_profile.id == p.id:
                    break
            else:
                profiles.append(last_profile)
            # print(profiles)
        random.shuffle(profiles)
        data = []
        for profile in profiles:
            serializer = ProfileSerializer(profile).data
            # print(dir(serializer))
            flag = False
            for like_id in like_users:
                if like_id['id'] == profile.user.id:
                    flag = True
                    break
    
            if flag:
                serializer['like'] = True
            else:
                serializer['like'] = False
            
            data.append(serializer)
    return Response(data)