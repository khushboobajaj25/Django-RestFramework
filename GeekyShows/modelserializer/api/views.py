import json
from django.shortcuts import render
import io
from api import models
from api import serializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(View):
    def get(Self,request,*args,**kwargs):
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
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = serializers.StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data created"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    def put(self,request,*args,**kwargs):
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
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = models.Student.objects.get(id=id)
        stu.delete()
        res = {"msg":"Data deleted"}
        return JsonResponse(res,safe=False)




        


