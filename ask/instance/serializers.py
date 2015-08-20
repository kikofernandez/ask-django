from .models import Service, Skill
from rest_framework import serializers
from django.contrib.auth.models import User

class ServiceSerializer(serializers.ModelSerializer):
    user_request = serializers.StringRelatedField()
    skills = serializers.StringRelatedField(many=True)
    state = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()

    def get_state(self, obj):
        return obj.get_state_display()

    def get_priority(self, obj):
        return obj.get_priority_display()


    class Meta:
        model = Service
        fields = ('id', 'request', 'user_request', 'assigned', 'skills', 'state', 'priority', 'no_people', 'cancellable')



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('tag',)
