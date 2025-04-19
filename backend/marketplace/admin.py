# marketplace/admin.py
from django.contrib import admin
from .models import Service, Subject
from .application.application_models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "price", "year", "is_finished")
    list_filter = ("is_finished", "year")
    search_fields = ("name", "user__username")
    filter_horizontal = ("services", "subjects")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
