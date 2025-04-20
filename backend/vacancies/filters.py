from django_filters import NumberFilter, BooleanFilter
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from vacancies.models import Vacancy


class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class VacancyFilters(django_filters.FilterSet):
    work_type = django_filters.NumberFilter(field_name="work_type__id")
    has_price = BooleanFilter(field_name="price", lookup_expr="isnull", exclude=True)
    job_experience = django_filters.NumberFilter(field_name="job_experience")
    stack = CharInFilter(field_name="stack__title", lookup_expr="in")

    class Meta:
        model = Vacancy
        fields = []
