from .application_models import Application
from rest_framework import serializers


class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class ApplicationListSerialier(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
