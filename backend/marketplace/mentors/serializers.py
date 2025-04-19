from rest_framework import serializers

from marketplace.mentors.models import Mentor

from marketplace.models import Service

from marketplace.serializers import ServiceSerializer, SubjectSerializer

from user.serializers import SocialNetworkUserSerializer


# rating
# photo


class GetListMentorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    rating = serializers.ReadOnlyField(source="user.bio.rating")
    photo = serializers.ImageField(
        source="user.bio.photo", read_only=True, use_url=True
    )
    full_name = serializers.SerializerMethodField()
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Mentor
        fields = (
            "username",
            "full_name",
            "services",
            "subjects",
            "rating",
            "photo",
            "count_successful_transactions",
        )

    def get_full_name(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).strip()


class GetDetailMentorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    full_name = serializers.SerializerMethodField()
    rating = serializers.ReadOnlyField(source="user.bio.rating")
    photo = serializers.ImageField(
        source="user.bio.photo", read_only=True, use_url=True
    )
    social_network = SocialNetworkUserSerializer(
        source="user.bio.social_networks", many=True, read_only=True
    )
    services = ServiceSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Mentor
        fields = (
            "username",
            "full_name",
            "description",
            "services",
            "rating",
            "photo",
            "subjects",
            "count_successful_transactions",
            "social_network",
        )

    def get_full_name(self, obj):
        return (obj.user.first_name + " " + obj.user.last_name).strip()
