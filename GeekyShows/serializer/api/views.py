import json
from django.http.response import JsonResponse
from django.shortcuts import render
from api import models
from api import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Model object single student data


def student_detail(request):
    stu = models.Student.objects.get(id=1)
    # print(stu)
    serializer = serializers.StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # convetring into python
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data)
# query set all student


def student_list(request):
    stu = models.Student.objects.all()
    serializer = serializers.StudentSerializer(stu, many=True)
    # print(serializer)
    # print(serializer.data)
    # convetring into python
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data, safe=False)
