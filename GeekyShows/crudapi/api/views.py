import json
from django.shortcuts import render
import io
from api import models
from api import serializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def studentapi(request):
    print(request.method)
    if request.method == "GET":
        print("hi")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        if id is not None:
            stu = models.Student.objects.get(id=id)
            serializer = serializers.StudentSerializer(stu)
            return JsonResponse(serializer.data)
        stu = models.Student.objects.all()
        serializer = serializers.StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
      
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = serializers.StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data created"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = models.Student.objects.get(id=id)
        serializer = serializers.StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Updated Data"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = models.Student.objects.get(id=id)
        stu.delete()
        res = {"msg":"Data deleted"}
        return JsonResponse(res,safe=False)
    
