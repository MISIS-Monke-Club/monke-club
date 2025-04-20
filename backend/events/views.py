from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer, EventCreateUpdateSerializer


class EventListCreateView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):

    def get(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)

    def put(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        serializer = EventCreateUpdateSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

