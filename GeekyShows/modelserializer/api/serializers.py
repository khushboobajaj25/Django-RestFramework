from django.db.models import fields
from rest_framework import serializers
from api import models

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = models.Student
        fields= "__all__"
        # read_only_fields=["name","roll"]
        extra_kwargs = {"name":{"read_only":True}}
