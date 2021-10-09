import json
import io


from django.shortcuts import render
from api import models
from api import serializers
from rest_framework.parsers import JSONParser

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Model object single student data


@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream=stream)
        serializer = serializers.StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data created"}

            return JsonResponse(res)
        return JsonResponse(serializer.errors)
