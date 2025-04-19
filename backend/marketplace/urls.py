from django.urls import path, include, re_path
from .views import BombiniGusiniSubject, BombiniGusiniService

urlpatterns = [
    path("mentors/", include("marketplace.mentors.urls")),
    re_path(r"^services/$", BombiniGusiniService.as_view(), name="service-list"),
    re_path(r"^subjects/$", BombiniGusiniSubject.as_view(), name="subject-list"),
]
