from rest_framework import serializers
from user.models import UserBio

from user.models import SocialNetwork

from user.rating import add_user_activity


class SocialNetworkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ("name", "text")


class UserBioSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username', read_only=True)
    full_name = serializers.CharField(required=False)
    rating = serializers.SerializerMethodField(read_only=True)
    social_networks = SocialNetworkUserSerializer(many=True, required=False)

    class Meta:
        model = UserBio
        fields = ("username", "full_name", "rating", "photo", "course", "faculty", "social_networks")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['full_name'] = f"{instance.user.first_name} {instance.user.last_name}".strip()
        return data

    def get_rating(self, obj):
        return obj.rating

    def update(self, instance, validated_data):
        social_networks_data = validated_data.pop('social_networks', None)

        full_name = validated_data.pop('full_name', None)

        if full_name:

            first_name, *rest = full_name.strip().split(" ", 1)
            last_name = rest[0] if rest else ""
            user = instance.user
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            add_user_activity(user, "filled_full_name")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if social_networks_data is not None:
            instance.social_networks.all().delete()

            for sn_data in social_networks_data:
                SocialNetwork.objects.create(user=instance, **sn_data)

            add_user_activity(instance.user, "added_socials")

        instance.save()
        return instance
