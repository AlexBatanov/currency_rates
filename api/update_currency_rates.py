import requests
import datetime

from api.models import CurrencyRate
from api.serializers import CurrencyCreateSerializer


class UpdateCurrencyRates:

    def update_currency(self):
        print('Обновление курса валют ...')
        self.__uploading_db()
        print('Обновление курса валют звершено')

    def __get_currencies(self):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        if response.status_code == 200:
            return response.json().get('Valute')
        raise Exception('Сервер не доступен')

    def __uploading_db(self):
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
            else:
                print(serializer.errors)
