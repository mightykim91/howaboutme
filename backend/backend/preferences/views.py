from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from profiles.models import Body, Education, Job, Area, Religion
from .serializers import PreferenceSerializer
from .models import Preference

class PreferenceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # try:
        iter_data = request.data.lists()
        data = {}
        many_fields = ['body','education','area','religion','job']
        for key,val in iter_data:
            if key not in many_fields:
                data[key] = val[0]
                continue
            data[key] = val
        print(data)
        
        tmp = []
        for name in data['body']:
            if name == "상관 없음":
                objects = Body.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Body, name=name).id)
        data['body'] = tmp
        print('---')
        tmp = []
        for name in data['education']:
            if name == "상관 없음":
                objects = Education.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            print(name)
            tmp.append(get_object_or_404(Education, name=name).id)
        data['education'] = tmp
        print('---')
        tmp = []
        for name in data['job']:
            if name == "상관 없음":
                objects = Job.objects.all()
                for obj in objects:
                    # print(obj)
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Job, name=name).id)
        data['job'] = tmp
        print('---')
        tmp = []
        for name in data['area']:
            if name == "모든 지역":
                objects = Area.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Area, name=name).id)
        data['area'] = tmp
        print('---')
        tmp = []
        for name in data['religion']:
            if name == "상관 없음":
                objects = Religion.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Religion, name=name).id)
        data['religion'] = tmp

        print(data)
        serializer = PreferenceSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data)
        # except:
        #     msg = {
        #         'msg':'fail'
        #     }
        #     return JsonResponse(msg, status=500)

    def put(self,request):
        instance = get_object_or_404(Preference, user=request.user)

        # try:
        iter_data = request.data.lists()
        data = {}
        many_fields = ['body','education','area','religion','job']
        for key,val in iter_data:
            if key not in many_fields:
                data[key] = val[0]
                continue
            data[key] = val
        # print(data)
        
        tmp = []
        for name in data['body']:
            if name == "상관 없음":
                objects = Body.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Body, name=name).id)
        data['body'] = tmp
        # print('---')
        tmp = []
        for name in data['education']:
            if name == "상관 없음":
                objects = Education.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            # print(name)
            tmp.append(get_object_or_404(Education, name=name).id)
        data['education'] = tmp
        # print('---')
        tmp = []
        for name in data['job']:
            if name == "상관 없음":
                objects = Job.objects.all()
                for obj in objects:
                    # print(obj)
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Job, name=name).id)
        data['job'] = tmp
        # print('---')
        tmp = []
        for name in data['area']:
            if name == "모든 지역":
                objects = Area.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Area, name=name).id)
        data['area'] = tmp
        # print('---')
        tmp = []
        for name in data['religion']:
            if name == "상관 없음":
                objects = Religion.objects.all()
                for obj in objects:
                    tmp.append(obj.id)
                break
            tmp.append(get_object_or_404(Religion, name=name).id)
        data['religion'] = tmp

        # print(data)
        serializer = PreferenceSerializer(instance,data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data)
        # except:
        #     msg = {
        #         'msg':'fail'
        #     }
        #     return JsonResponse(msg, status=500)

    def delete(self, request):
        preference = get_object_or_404(Preference, user=request.user)
        preference.delete()
        return JsonResponse({'msg':'delete success'}, status=200)