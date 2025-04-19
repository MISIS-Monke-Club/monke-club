from django.urls import path, include

urlpatterns = [
    path("mentors/", include("marketplace.mentors.urls")),
]
