from rest_framework import viewsets, filters, permissions
from django.db.models import F
from vacancies.models import Vacancy,WorkType,Stack
from vacancies.serializers import WorkTypeSerializer,ListVacancySerializer,StackSerializer,DetailVacancySerializer,CreateVacancySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from user.mixins import IsOwnerMixin
from marketplace.mentors.filters import *
from .handler import GeVacancyFiltersEndpoint
from .filters import VacancyFilters



class VacanciesViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = VacancyFilters
    ordering_fields = ["data_created", "price"]
    ordering = ['-data_created']

    ordering_labels = {
        "data_created": "Сначала давно добавленные",
        "-data_created": "Сначала недавно добавленные",
        "price": "Сначала с зарплатой ниже",
        "-price": "Сначала с зарплатой выше",
    }

    def get_serializer_class(self):
        if self.action == "list":
            return ListVacancySerializer
        elif self.action == "retrieve":
            return DetailVacancySerializer
        else:
            return CreateVacancySerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update":
            return [IsOwnerMixin()]
        else:
            return [permissions.AllowAny()]

    @action(detail=False, methods=["get"], url_path="ordering-fields")
    def get_ordering_fields(self, request):
        result = []
        for index, data in self.ordering_labels.items():
            result.append({"value": index, "label": data})
        return Response(result)

    @action(detail=False, methods=["get"], url_path="filters")
    def get_filter_fields(self, request):
        result = GeVacancyFiltersEndpoint().get_filters()
        return Response(result)