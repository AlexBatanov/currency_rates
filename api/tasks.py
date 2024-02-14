from celery import shared_task

from .update_currency_rates import UpdateCurrencyRates

@shared_task
def my_task():
    UpdateCurrencyRates().update_currency()
