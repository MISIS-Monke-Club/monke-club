from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path("", include("auth_app.urls")),
    path("profile/", include("user.urls")),
    path('marketplace/', include('marketplace.urls')),
    path('vacancies/', include('vacancies.urls')),
]
