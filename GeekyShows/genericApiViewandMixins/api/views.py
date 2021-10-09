from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import models
from api import serializers
from  rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin 
from rest_framework.mixins import CreateModelMixin 
from rest_framework.mixins import RetrieveModelMixin 
from rest_framework.mixins import UpdateModelMixin 
from rest_framework.mixins import DestroyModelMixin 
 
from rest_framework import status


class StudentList(GenericAPIView,ListModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentReterieve(GenericAPIView,RetrieveModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

   





        
