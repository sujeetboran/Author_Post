from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'


class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = authors
        fields = '__all__'
