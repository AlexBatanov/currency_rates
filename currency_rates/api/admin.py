from django.contrib import admin

from .models import CurrencyRate


@admin.register(CurrencyRate)
class BookAdmin(admin.ModelAdmin):
    list_display = ('charcode', 'rate', 'date')
    list_filter = ('charcode', 'date')
