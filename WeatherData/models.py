from django.db import models


class WeatherData(models.Model):
    location = models.ForeignKey('Location.Location', on_delete=models.CASCADE, related_name='weatherdata')
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    precipitation = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)