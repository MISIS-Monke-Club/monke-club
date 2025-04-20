import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from marketplace.mentors.models import Mentor

class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class MentorFilters(django_filters.FilterSet):
    course = django_filters.NumberFilter(field_name="user__bio__course")
    subjects = CharInFilter(field_name="subjects__name", lookup_expr="in")
    services = CharInFilter(field_name="services__name", lookup_expr="in")

    class Meta:
        model = Mentor
        fields = []