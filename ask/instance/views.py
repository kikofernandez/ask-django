from django.shortcuts import render

# Create your views here.
from instance.models import Skill, Service
from instance.serializers import SkillSerializer, ServiceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ServiceList(APIView):
    """
    List all services, or create a new service
    """
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


    # TODO: http://www.django-rest-framework.org/tutorial/3-class-based-views/
    def post(self, request, format=None):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

# TODO: http://www.django-rest-framework.org/tutorial/3-class-based-views/
class ServiceDetail(APIView):
    """
    Retrieve, update or delete a service
    """

    def get_object(self, pk):
        raise Http404

    def get(self, request, pk, format=None):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response([], status=status.HTTP_400_BAD_REQUEST)
