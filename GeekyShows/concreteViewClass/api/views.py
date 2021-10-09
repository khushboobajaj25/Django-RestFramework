
from api import models
from api import serializers

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView,RetrieveAPIView
 
from rest_framework import status

# Concrete View Classes
class StudentList(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# INstead of using the four above classes we can use 2 classes below
class StudentListCreate(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer







        
