from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Sum, Max
from .models import WeatherData
from .serializers import WeatherDataSerializer

# WEATHER-DATA
class WeatherDataCreateAPIView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class WeatherDataUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class WeatherDataLocationAPIView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return WeatherData.objects.filter(location_id=location_id)


# ANALYTICS (Tahlillar)
class TemperatureAverageAPIView(APIView):
    def get(self, request):
        avg_temp = WeatherData.objects.aggregate(avg_temperature=Avg('temperature'))['avg_temperature']
        return Response({"average_temperature": avg_temp})


class PrecipitationSumAPIView(APIView):
    def get(self, request):
        total_precipitation = WeatherData.objects.aggregate(total_precipitation=Sum('precipitation'))['total_precipitation']
        return Response({"total_precipitation": total_precipitation})


class WindSpeedMaxAPIView(APIView):
    def get(self, request):
        max_wind_speed = WeatherData.objects.aggregate(max_wind_speed=Max('wind_speed'))['max_wind_speed']
        return Response({"max_wind_speed": max_wind_speed})