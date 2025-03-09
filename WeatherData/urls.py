from django.urls import path
from .views import (
    WeatherDataCreateAPIView, WeatherDataUpdateAPIView, WeatherDataLocationAPIView,
    TemperatureAverageAPIView, PrecipitationSumAPIView, WindSpeedMaxAPIView
)

app_name = 'weatherdata'

urlpatterns = [
    # WEATHER-DATA
    path('weather-data/', WeatherDataCreateAPIView.as_view(), name='weather-data-create'),
    path('weather-data/<int:pk>/', WeatherDataUpdateAPIView.as_view(), name='weather-data-update'),
    path('weather-data/location/<int:location_id>/', WeatherDataLocationAPIView.as_view(),
         name='weather-data-by-location'),

    # ANALYTICS (Tahlillar)
    path('analytics/temperature-avg/', TemperatureAverageAPIView.as_view(), name='temperature-avg'),
    path('analytics/precipitation-sum/', PrecipitationSumAPIView.as_view(), name='precipitation-sum'),
    path('analytics/wind-speed-max/', WindSpeedMaxAPIView.as_view(), name='wind-speed-max'),
]