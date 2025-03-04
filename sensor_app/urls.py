from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/sensor-data/', views.receive_sensor_data, name='sensor_data'),
]