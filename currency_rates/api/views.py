from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CurrencyRate
from .serializers import CurrencyCreateSerializer, CurrencySerializer


class CurrencyRateViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencySerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CurrencySerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CurrencyCreateSerializer
        return CurrencySerializer

    def retrieve(self, request):
        charcode = request.query_params.get('charcode')
        date = request.query_params.get('date')

        currency_rate = get_object_or_404(
            self.get_queryset(), charcode=charcode, date=date
        )
        serializer = self.get_serializer(currency_rate)

        return Response(serializer.data)
