import django_filters
from marketplace.mentors.models import Mentor


class MentorFilters(django_filters.FilterSet):
    course = django_filters.NumberFilter(field_name="user__bio__course")
    subject = django_filters.CharFilter(
        field_name="subjects__name", lookup_expr="iexact"
    )
    services = django_filters.CharFilter(
        field_name="services__name", lookup_expr="iexact"
    )

    class Meta:
        model = Mentor
        fields = []
