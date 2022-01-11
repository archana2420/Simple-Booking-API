from django.contrib import admin
from django.urls import path,include
from .views import BookingAPIView,BookingsCancelAPIView

urlpatterns = [
    path('booking/',BookingAPIView.as_view()),
    path('cancel/',BookingsCancelAPIView.as_view()),
]