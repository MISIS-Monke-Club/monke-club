from rest_framework import serializers
from .models import Event, EventType


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ["type_name"]


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'location', 'image','slug']
        extra_kwargs = {"slug": {"read_only": True}}


class EventDetailSerializer(serializers.ModelSerializer):
    event_type = EventTypeSerializer(read_only=True)
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'date',
            'price',
            'location',
            'description',
            'registration_link',
            'event_type',
            'image',
            'slug',
        ]
        extra_kwargs = {"slug": {"read_only": True}}

class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'date',
            'price',
            'location',
            'description',
            'registration_link',
            'event_type',
            'image',
        ]
        extra_kwargs = {"slug": {"read_only": True}}