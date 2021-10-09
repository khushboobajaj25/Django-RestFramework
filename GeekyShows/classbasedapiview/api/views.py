from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import models
from api import serializers
from  rest_framework.views import APIView
from rest_framework import status


class StudentView(APIView):
    def get(self,request,format=None):
        id = request.data.get("id")
        if id :
            stu = models.Student.objects.get(id = id)
            serializer = serializers.StudentSerializer(stu)
            return Response(serializer.data,status = status.HTTP_200_OK)
        stu = models.Student.objects.all()
        serializer= serializers.StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self,request,format =None):
        data = request.data
        serializer = serializers.StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data created"})
        return Response(serializer.errors)
    def put(self,request,format=None):
        id = request.data.get("id")
        stu = models.Student.objects.get(pk=id)
        serializer = serializers.StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors)
    def delete(Self,request,format=None):
        id = request.data.get("id")
        stu = models.Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data deleted"},status=status.HTTP_200_OK)






        
