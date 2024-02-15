from django.urls import path

from .views import CurrencyRateViewSet

urlpatterns = [
    path('', CurrencyRateViewSet.as_view({'get': 'retrieve'}), name='custom-rate'),
]
