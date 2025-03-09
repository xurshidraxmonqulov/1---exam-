from django.urls import path
from .views import LocationCreateAPIView, LocationUpdateAPIView

App_name = 'Location'

urlpatterns = [
    path('locations/', LocationCreateAPIView.as_view(), name='location-create'),
    path('locations/<int:pk>/', LocationUpdateAPIView.as_view(), name='location-detail'),
]