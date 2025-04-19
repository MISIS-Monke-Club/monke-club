from django.urls import path, include

urlpatterns = [
    path("applications/", include("marketplace.application.applications_urls")),
]
