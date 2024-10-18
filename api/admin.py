from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'created_at', 'updated_at')
