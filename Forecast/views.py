from rest_framework import generics
from .models import Forecast
from .serializers import ForecastSerializer


class ForecastCreateAPIView(generics.ListCreateAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer


class ForecastUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer


class ForecastLocationAPIView(generics.ListAPIView):
    serializer_class = ForecastSerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Forecast.objects.filter(location_id=location_id)


from django.shortcuts import render

# Create your views here.
