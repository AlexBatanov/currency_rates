import requests
import datetime
from http import HTTPStatus

from django.core.management.base import BaseCommand

from api.models import CurrencyRate
from api.serializers import CurrencyCreateSerializer


class Command(BaseCommand):
    help = 'Получает текущий курс валют и записывает в бд'

    def handle(self, *args, **options) -> None:
        self.stdout.write('Обновление курса валют ...')
        self.__uploading_db()
        self.stdout.write('Обновление курса валют звершено')

    def __get_currencies(self) -> dict:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

        if response.status_code == HTTPStatus.OK:
            return response.json().get('Valute')
        raise Exception('Сервер не доступен')

    def __uploading_db(self) -> None:
        currencies = self.__get_currencies()

        for value in currencies.values():
            current_date = datetime.datetime.now().date()
            charcode = value.get('CharCode')

            currency_rate = CurrencyRate.objects.filter(
                date=current_date, charcode=charcode
            ).first()

            if currency_rate:
                serializer = CurrencyCreateSerializer(
                    instance=currency_rate, data=value
                )
            else:
                serializer = CurrencyCreateSerializer(data=value)
            if serializer.is_valid():
                serializer.save()
