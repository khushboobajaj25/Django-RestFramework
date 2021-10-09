from rest_framework import serializers
from api import models
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields="__all__"