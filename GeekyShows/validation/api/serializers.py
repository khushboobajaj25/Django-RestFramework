from rest_framework import serializers
from api import models
# Validators

def start_with_r(value):
    if value[0].lower()!="r":
        raise serializers.ValidationError("Error")
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70, validators=[start_with_r])
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

    #  field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats full")
        return value
    def validate(Self,data):
        name = data.get("name")
        city = data.get("city")
        if name.lower() !="ayush":
            raise serializers.ValidationError("error")
    

