from django_filters import rest_framework as filters
from .application_models import Application


class ApplicationFilter(filters.FilterSet):
    subjects = filters.ModelMultipleChoiceFilter(
        field_name="subjects__name",
        to_field_name="name",
        queryset=Application._meta.get_field("subjects").related_model.objects.all(),
        label="Предметы",
    )
    services = filters.ModelMultipleChoiceFilter(
        field_name="services__name",
        to_field_name="name",
        queryset=Application._meta.get_field("services").related_model.objects.all(),
        label="Тип задачи",
    )
    year = filters.NumberFilter(field_name="year", label="Курс")

    is_free = filters.BooleanFilter(method="filter_is_free", label="Бесплатно")

    def filter_is_free(self, queryset, name, value):
        if value:
            return queryset.filter(price=0)
        return queryset.exclude(price=0)

    class Meta:
        model = Application
        fields = ["subjects", "services", "year", "is_free"]
