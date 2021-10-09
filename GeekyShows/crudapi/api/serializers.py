from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)
    def create(self, validated_data):
        return models.Student.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        print(instance.roll)
        instance.city = validated_data.get('city',instance.city)
        print(instance.city)
        instance.save()
        return instance