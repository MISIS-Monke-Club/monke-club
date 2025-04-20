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
from rest_framework.permissions import IsAuthenticated,AllowAny


class ApplicationListCreateView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Application.objects.all().prefetch_related("subjects", "services")
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter, 
    )
    filterset_class = ApplicationFilter
    ordering_fields = ["date_of_creation", "price"]
    ordering = ["-date_of_creation"]

    search_fields = [
        "name",
        "description",
        "subjects__name",
        "services__name",
    ]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

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
    

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ApplicationFilterFieldsView(APIView):

    permission_classes=[AllowAny]

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
    permission_classes=[AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            "ordering_fields": [
                "date_of_creation",
                "price"
            ]
        })