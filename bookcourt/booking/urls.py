from django.urls import path, include

from .views import BookingView

urlpatterns = [
    path('', BookingView.as_view(), name='booking'),
]
