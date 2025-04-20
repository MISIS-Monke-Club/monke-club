from rest_framework import serializers
from user.models import UserBio

from user.models import SocialNetwork



class SocialNetworkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ("name", "text")



class UserBioSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username', read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)
    social_networks = SocialNetworkUserSerializer(many=True, required=False)

    class Meta:
        model = UserBio
        fields = ("username", "full_name", "rating", "photo", "course", "faculty", "social_networks")

    def get_rating(self, obj):
        return obj.rating

    def get_full_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def update(self, instance, validated_data):
        social_networks_data = validated_data.pop('social_networks', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if social_networks_data is not None:
            instance.social_networks.all().delete()
            for sn_data in social_networks_data:
                SocialNetwork.objects.create(user=instance, **sn_data)

        instance.save()
        return instance