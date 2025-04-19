from django.contrib import admin

from marketplace.mentors.models import Mentor

from marketplace.models import Service

from marketplace.models import Subject




@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    fields = ("user", "services", "subjects", "description", "count_successful_transactions")
    filter_horizontal = ("services", "subjects")




@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ("name", )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    fields = ("name", )