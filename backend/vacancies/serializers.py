from django.template.context_processors import request
from rest_framework import serializers
from vacancies.models import Vacancy
from vacancies.models import WorkType, Stack
from django.utils import timezone


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = ("title", )

class ListVacancySerializer(serializers.ModelSerializer):
    work_type = WorkTypeSerializer(read_only=True)
    class Meta:
        model = Vacancy
        fields = ("title", "slug", "price", "work_type", "job_experience")

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ("title", )

class DetailVacancySerializer(serializers.ModelSerializer):
    work_type = serializers.PrimaryKeyRelatedField(
        queryset=WorkType.objects.all(),
        required=False,
    )
    stack = serializers.PrimaryKeyRelatedField(
        queryset=Stack.objects.all(),
        many=True,
        required=False
    )
    data_created = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = ("title", "description", "stack", "data_created", "data_end","schedule", "work_space",  "price", "work_type", "job_experience")

    def get_data_created(self, obj):
        return timezone.localtime(obj.data_created).strftime("%H:%M %d %b %Y")

    def create(self, validated_data):
        stack = validated_data.pop("stack", [])
        user = self.context["request"].user
        vacancy = Vacancy.objects.create(user=user, **validated_data)
        if stack:
            vacancy.stack.set(stack)
        return vacancy
    
class CreateVacancySerializer(serializers.ModelSerializer):
    stack = serializers.PrimaryKeyRelatedField(
        queryset=Stack.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Vacancy
        fields = ("title", "description", "stack", "data_end", "schedule",
                  "work_space", "price", "work_type", "job_experience")

    def create(self, validated_data):
        stack = validated_data.pop("stack", [])
        user = self.context["request"].user
        vacancy = Vacancy.objects.create(user=user, **validated_data)
        if stack:
            vacancy.stack.set(stack)
        return vacancy