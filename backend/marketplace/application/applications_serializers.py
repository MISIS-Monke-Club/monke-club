from .application_models import Application
from rest_framework import serializers
from marketplace.serializers import ServiceSerializer, SubjectSerializer
from marketplace.models import Service, Subject


class ApplicationsSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), many=True, write_only=True
    )
    subjects = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), many=True, write_only=True
    )
    services_detail = ServiceSerializer(source='services', many=True, read_only=True)
    subjects_detail = SubjectSerializer(source='subjects', many=True, read_only=True)

    class Meta:
        model = Application
        fields = "__all__"
        extra_kwargs = {
            "slug": {"read_only": True}
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["services"] = rep.pop("services_detail")
        rep["subjects"] = rep.pop("subjects_detail")
        return rep

    def create(self, validated_data):
        services_ids = validated_data.pop("services", [])
        subjects_ids = validated_data.pop("subjects", [])
        
        application = super().create(validated_data)

        # Устанавливаем по id
        application.services.set(Service.objects.filter(id__in=[s.id if isinstance(s, Service) else s for s in services_ids]))
        application.subjects.set(Subject.objects.filter(id__in=[s.id if isinstance(s, Subject) else s for s in subjects_ids]))
    
        return application

    def update(self, instance, validated_data):
        services_ids = validated_data.pop("services", None)
        subjects_ids = validated_data.pop("subjects", None)

        instance = super().update(instance, validated_data)

        if services_ids is not None:
            instance.services.set(Service.objects.filter(id__in=[s.id if isinstance(s, Service) else s for s in services_ids]))
        if subjects_ids is not None:
            instance.subjects.set(Subject.objects.filter(id__in=[s.id if isinstance(s, Subject) else s for s in subjects_ids]))

        return instance


class ApplicationCreateSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Subject.objects.all(), write_only=True
    )
    services = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Service.objects.all(), write_only=True
    )

    class Meta:
        model = Application
        fields = "__all__"
        extra_kwargs = {"slug": {"read_only": True}}


class ApplicationListSerializer(serializers.ModelSerializer):
    services = SubjectSerializer(many=True, read_only=True)
    subjects = ServiceSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Application
        fields = [
            "name",
            "username",
            "year",
            "subjects",
            "services",
            "date_of_creation",
            "price",
            "slug",
        ]
        extra_kwargs = {"slug": {"read_only": True}}
