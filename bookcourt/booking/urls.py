from django.urls import path, include

from .views import *

urlpatterns = [
    path('', BookingView.as_view(), name='booking'),
    path("confirmation/", BookingConfirmationView.as_view(), name="confirmation"),
]
