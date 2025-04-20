from django_filters import rest_framework as filters
from .models import Event, EventType

class EventFilter(filters.FilterSet):
    event_types = filters.ModelMultipleChoiceFilter(
        field_name="event_type__type_name",
        to_field_name="type_name",
        queryset=EventType.objects.all(),
        label="Тип мероприятия"
    )
    
    is_free = filters.BooleanFilter(
        method="filter_is_free",
        label="Бесплатно"
    )

    def filter_is_free(self, queryset, name, value):
        if value:
            return queryset.filter(price=0)
        return queryset

    class Meta:
        model = Event
        fields = ["event_types", "is_free"]