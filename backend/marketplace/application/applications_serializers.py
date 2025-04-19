from .application_models import Application
from rest_framework import serializers
from marketplace.serializers import ServiceSerializer, SubjectSerializer
from marketplace.models import Service, Subject


class ApplicationsSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    extra_kwargs = {
            'slug': {'read_only': True}
        }

    class Meta:
        model = Application
        fields = "__all__"


class ApplicationCreateSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Service.objects.all(), write_only=True
    )
    services = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Subject.objects.all(), write_only=True
    )
    extra_kwargs = {
            'slug': {'read_only': True}
        }

    class Meta:
        model = Application
        fields = "__all__"


class ApplicationListSerializer(serializers.ModelSerializer):
    services = SubjectSerializer(many=True, read_only=True)
    subjects = ServiceSerializer(many=True, read_only=True)
    extra_kwargs = {
            'slug': {'read_only': True}
        }

    class Meta:
        model = Application
        fields = ["name", "year", "subjects", "services", "date_of_creation", "price"]
