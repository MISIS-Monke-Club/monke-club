from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("auth_app.urls")),
    path("api/", include("user.urls")),
    path("marketplace/", include("marketplace.urls")),
]
