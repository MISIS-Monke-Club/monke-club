# marketplace/admin.py
from django.contrib import admin
from .models import Service, Subject
from .application.application_models import Application
from marketplace.mentors.models import Mentor


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "price", "year", "is_finished")
    list_filter = ("is_finished", "year")
    search_fields = ("name", "user__username")


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "services",
        "subjects",
        "description",
        "count_successful_transactions",
    )
    filter_horizontal = ("services", "subjects")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    fields = ("name",)