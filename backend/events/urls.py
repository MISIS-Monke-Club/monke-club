from django.urls import path
from .views import EventListCreateView, EventDetailView

urlpatterns = [
    path("", EventListCreateView.as_view(), name='event-list-create'), 
    path("<slug:slug>/", EventDetailView.as_view(), name='event-detail'),
]