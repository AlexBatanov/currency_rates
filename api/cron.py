from api.models import CurrencyRate

def my_cron_job():
    obj = CurrencyRate(charcode='a', rate=1.1)
    obj.save()