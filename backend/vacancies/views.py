from django.shortcuts import render
from rest_framework import viewsets

from vacancies.models import Vacancy

from vacancies.serializers import ListVacancySerializer

from vacancies.serializers import DetailVacancySerializer


class VacanciesViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == 'list':
            return ListVacancySerializer
        elif self.action == 'retrieve':
            return DetailVacancySerializer
        elif self.action == 'create':
            return DetailVacancySerializer

        return ListVacancySerializer

