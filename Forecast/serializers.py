from rest_framework import serializers
from .models import Forecast
from Location.serializers import LocationSerializer


class ForecastSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Forecast
        fields = (
            'id', 'location', 'forecast_date', 'temperature_min',
            'temperature_max', 'humidity', 'precipitation_probability',
            'wind_speed', 'wind_direction', 'created_at'
        )
