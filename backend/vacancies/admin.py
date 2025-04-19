from django.contrib import admin
from .models import Vacancy, WorkType, Stack


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "work_type", "price", "data_created", "data_end")
    list_filter = ("work_type", "data_created", "data_end")
    search_fields = ("title", "description", "work_space", "schedule")
    filter_horizontal = ("stack",)
    ordering = ("-data_created",)


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)