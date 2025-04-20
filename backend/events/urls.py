from django.urls import path
from .views import EventListCreateView, EventDetailView , EventFilterFieldsView,EventOrderingFieldsView,EventTypeListView

urlpatterns = [
    path('event-types/', EventTypeListView.as_view(), name='event-type-list'),
    path('filter-fields/', EventFilterFieldsView.as_view(), name='event-filter-fields'),
    path('ordering-fields/', EventOrderingFieldsView.as_view(), name='event-ordering-fields'),
    path("", EventListCreateView.as_view(), name='event-list-create'), 
    path("<slug:slug>/", EventDetailView.as_view(), name='event-detail'),
]