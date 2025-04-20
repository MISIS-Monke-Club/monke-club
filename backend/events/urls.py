from django.urls import path
from .views import EventListCreateView, EventDetailView , EventFilterFieldsView,EventOrderingFieldsView,EventTypeListView

urlpatterns = [
    path("", EventListCreateView.as_view(), name='event-list-create'), 
    path("<slug:slug>/", EventDetailView.as_view(), name='event-detail'),
    path('events/filter-fields/', EventFilterFieldsView.as_view()),
    path('events/ordering-fields/', EventOrderingFieldsView.as_view()),
    path('event-types/', EventTypeListView.as_view()),
]