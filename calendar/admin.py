from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Event, EventAdmin)
