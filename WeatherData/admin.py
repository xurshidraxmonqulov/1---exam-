from django.contrib import admin
from .models import WeatherData


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('location', 'temperature', 'humidity', 'precipitation', 'wind_speed', 'recorded_at')
    list_filter = ('location', 'recorded_at')
    search_fields = ('location__name',)
    date_hierarchy = 'recorded_at'

    fieldsets = (
        ('Location Information', {
            'fields': ('location',)
        }),
        ('Weather Measurements', {
            'fields': ('temperature', 'humidity', 'pressure', 'precipitation')
        }),
        ('Wind Information', {
            'fields': ('wind_speed', 'wind_direction')
        }),
    )

    readonly_fields = ('recorded_at',)