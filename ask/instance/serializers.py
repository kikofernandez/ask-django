from .models import Service, Skill
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'request', 'user_request', 'assigned', 'skills')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('tag',)
