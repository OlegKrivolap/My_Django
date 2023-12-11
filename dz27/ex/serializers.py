from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
