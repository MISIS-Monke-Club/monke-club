from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from .models import Event,EventType
from .serializers import EventListSerializer, EventDetailSerializer, EventCreateUpdateSerializer,EventTypeSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EventFilter
from rest_framework.views import APIView
from rest_framework.response import Response


class EventListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Event.objects.all()
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  
    filterset_class = EventFilter
    ordering_fields = ['price', 'date']  
    ordering = ['-date']  

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EventCreateUpdateSerializer
        return EventListSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return EventCreateUpdateSerializer
        return EventDetailSerializer
    lookup_field = "slug"

    def get(self, request, slug, *args, **kwargs):
        return self.retrieve(request, slug=slug, *args, **kwargs)

    def put(self, request, slug, *args, **kwargs):
        return self.update(request, slug=slug, *args, **kwargs)

    def delete(self, request, slug, *args, **kwargs):
        return self.destroy(request, slug=slug, *args, **kwargs)
    
class EventFilterFieldsView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "fields": {
                "event_types": "Тип мероприятия",
                "is_free": "Бесплатно",
                "price_min": "Минимальная цена",
                "price_max": "Максимальная цена",
                "start_date": "Дата начала (ГГГГ-ММ-ДД)",
                "end_date": "Дата окончания (ГГГГ-ММ-ДД)",
                "location": "Местоположение"
            }
        })

class EventOrderingFieldsView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "ordering_fields": [
                "date",
                "-date",
                "price",
                "-price"
            ]
        })

class EventTypeListView(GenericAPIView, ListModelMixin):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)