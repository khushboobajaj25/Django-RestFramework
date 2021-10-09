from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validate_data):
        return models.Student.objects.create(**validate_data)
