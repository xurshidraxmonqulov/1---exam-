from rest_framework import serializers
from .models import WeatherData
from Location.serializers import LocationSerializer


class WeatherDataSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = WeatherData
        fields = ['id', 'location', 'temperature', 'humidity',
                  'pressure', 'wind_speed', 'wind_direction',
                  'precipitation', 'recorded_at']