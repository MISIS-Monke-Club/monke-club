from django.contrib.auth.models import User
from rest_framework import serializers

from marketplace.mentors.models import Mentor

from marketplace.models import Service
from marketplace.models import Subject

from marketplace.serializers import ServiceSerializer, SubjectSerializer

from user.serializers import SocialNetworkUserSerializer





class GetListMentorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    rating = serializers.ReadOnlyField(source='user.bio.rating')
    photo = serializers.ImageField(source='user.bio.photo', read_only=True, use_url=True)
    full_name = serializers.SerializerMethodField()
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Mentor
        fields = ("username", "full_name", "services", "subjects", "rating", "photo", "count_successful_transactions")


    def get_full_name(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).strip()



class GetDetailMentorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    full_name = serializers.SerializerMethodField()
    rating = serializers.ReadOnlyField(source='user.bio.rating')
    photo = serializers.ImageField(source='user.bio.photo', read_only=True, use_url=True)
    social_network = SocialNetworkUserSerializer(
        source='user.bio.social_networks',
        many=True,
        read_only=True
    )
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Mentor
        fields = ("username", "full_name", "description", "services", "rating", "photo",  "subjects", "count_successful_transactions", "social_network")

    def get_full_name(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).strip()



class MentorCreateSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, required=False)
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True, required=False)

    class Meta:
        model = Mentor
        fields = (
            "services",
            "subjects",
            "description",
            "count_successful_transactions"
        )

    def create(self, validated_data):
        services = validated_data.pop("services", [])
        subjects = validated_data.pop("subjects", [])
        user = self.context["request"].user
        mentor = Mentor.objects.create(user=user, **validated_data)
        mentor.services.set(services)
        mentor.subjects.set(subjects)
        return mentor

    def update(self, instance, validated_data):
        services = validated_data.pop("services", None)
        subjects = validated_data.pop("subjects", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if services:
            instance.services.set(services)
        if subjects:
            instance.subjects.set(subjects)

        instance.save()
        return instance

