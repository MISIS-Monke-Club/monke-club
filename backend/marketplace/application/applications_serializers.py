from .application_models import Application
from rest_framework import serializers
from marketplace.serializers import ServiceSerializer,SubjectSerializer


class ApplicationsSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Application
        fields = "__all__"


class ApplicationListSerialier(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Application
        fields = ['name','year','subjects','services','date_of_creation','price']
