from django.urls import path
from .views import schedule, appointments, times

urlpatterns = [
    path('', schedule, name='schedule'),
    path('/appointments/<int:id>/', appointments, name='appointments'),
    path('/appointments/<int:id>/times', times, name='times'),
]
