from rest_framework import mixins, generics
from .application_models import Application
from .applications_serializers import (
    ApplicationsSerializer,
    ApplicationListSerializer,
    ApplicationCreateSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as filters
from .application_filters import ApplicationFilter
from rest_framework.views import APIView
from rest_framework.response import Response


class ApplicationListCreateView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Application.objects.all().prefetch_related("subjects", "services")
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ApplicationFilter
    ordering_fields = ["date_of_creation", "price"]
    ordering = ["-date_of_creation"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ApplicationCreateSerializer
        return ApplicationListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApplicationRUDView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Application.objects.all()
    serializer_class = ApplicationsSerializer
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ApplicationFilterFieldsView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({
            "fields": {
                "subjects": "Предметы",
                "services": "Тип задачи",
                "year": "Курс",
                "is_free": "Бесплатно"
            }
        })


class ApplicationOrderingFieldsView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({
            "ordering_fields": [
                "date_of_creation",
                "price"
            ]
        })