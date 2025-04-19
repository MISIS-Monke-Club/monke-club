from django.urls import path
from .application_views import (
    ApplicationListCreateView as Alcv,
    ApplicationRUDView as Arud,
)

urlpatterns = [
    path("", Alcv.as_view(), name="application-list-create"),
    path("<str:username>/", Arud.as_view(), name="application-detail"),
]
