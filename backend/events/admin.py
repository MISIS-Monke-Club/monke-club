from django.contrib import admin
from .models import Event, EventType


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')  
    search_fields = ('type_name',) 


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'price', 'location', 'event_type', 'slug') 
    list_filter = ('event_type', 'date', 'location')  
    search_fields = ('title', 'description', 'location') 
    prepopulated_fields = {'slug': ('title',)}  
    date_hierarchy = 'date' 
    ordering = ('date',)  