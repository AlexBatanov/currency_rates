import datetime

from django.db import models


class CurrencyRate(models.Model):
    charcode: str = models.CharField(max_length=3)
    rate: float = models.FloatField()
    date: datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.charcode} - {self.rate}'
