from rest_framework import serializers

from .models import CurrencyRate


class CurrencyCreateSerializer(serializers.ModelSerializer):
    CharCode = serializers.CharField(source='charcode')
    Value = serializers.CharField(source='rate')

    class Meta:
        model = CurrencyRate
        fields = ['CharCode', 'Value']


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyRate
        fields = ['charcode', 'rate', 'date']
