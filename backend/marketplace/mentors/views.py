
from rest_framework import viewsets, filters, permissions
from django.db.models import F


from marketplace.mentors.models import Mentor

from marketplace.mentors.serializers import GetListMentorSerializer

from marketplace.mentors.serializers import GetDetailMentorSerializer, MentorCreateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from user.mixins import IsOwnerMixin
from marketplace.mentors.filters import *

from marketplace.mentors.handler import GeFiltersEndpoint


class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    lookup_field = 'user__username'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = MentorFilters
    ordering_fields = ["count_successful_transactions", "rating"]
    ordering = ['-count_successful_transactions']

    ordering_labels = {
        "count_successful_transactions": "Успешных сделок (по возрастанию)",
        "-count_successful_transactions": "Успешных сделок (по убыванию)",
        "rating": "Рейтинг (по убыванию)",
        "-rating": "Рейтинг (по убыванию)",
    }

    def get_queryset(self):
        return Mentor.objects.select_related('user__bio').annotate(
            rating=F('user__bio__rating')
        )

    def get_serializer_class(self):
        if self.action == "list":
            return GetListMentorSerializer

        elif self.action == "retrieve":
            return GetDetailMentorSerializer
        else:
            return MentorCreateSerializer

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
        result = GeFiltersEndpoint().get_filters()
        return result



