from rest_framework import serializers

from user.models import SocialNetwork


class SocialNetworkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ("name", "text")