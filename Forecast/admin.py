from django.contrib import admin
from .models import Forecast


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('location', 'forecast_date', 'temperature_min', 'temperature_max', 'humidity', 'precipitation_probability', 'wind_speed', 'wind_direction', 'created_at')
    list_filter = ('forecast_date', 'location')
    search_fields = ('location__name', 'forecast_date')