
from api import models
from api import serializers
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView
 
from rest_framework import status

# List and Create- Pk Not Required
class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


# Reterieve ,Update, delete required Pk
class StudentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



   





        
