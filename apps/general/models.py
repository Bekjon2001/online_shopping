from decimal import Decimal

import requests
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now
from django.core.cache import cache

from .validation_phone import check_uzb_number


class General(models.Model):
    class Currency(models.TextChoices):
        USD = 'USD', 'USD'
        EUR = 'EUR', 'EUR'
        RUB = 'RUB', 'RUB'
        UZS = 'UZS', 'UZS'

    DEFAULT_CURRENCY = Currency.UZS

    text = models.CharField(max_length=120)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(help_text="Email address")
    phone = models.CharField(max_length=13, validators=[check_uzb_number], help_text="UZB Number +998123456789")

    logo = models.ImageField(upload_to="general/logo/image/%Y/%m/%d/")
    cart_shipping_percent = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    class Meta:
        verbose_name = "General"
        verbose_name_plural = "General"

    def save(self, *args, **kwargs):
        self.cart_shipping_percent = Decimal(self.cart_shipping_percent)
        super().save(*args, **kwargs)

    def clean(self):
        if self.pk and General.objects.exists():
            raise ValidationError('Unique')

    def __str__(self):
        return self.text


class GeneralSocialMedia(models.Model):
    url = models.URLField()
    icon = models.ImageField(upload_to="social_links/icon/image/%Y/%m/%d/")


class CurrencyAmount(models.Model):
    GET_CURRENCY_URL = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{currency}/all/{date}/'

    currency = models.CharField(max_length=10, choices=General.Currency.choices)
    usd_amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()

    @classmethod
    def get_amount(cls, currency: str):
        today = now().date()

        amount_in_uzs = cache.get(f'{currency}_{today}')

        if not amount_in_uzs:
            obj, created = cls.objects.get_or_create(
                currency=currency,
                date=today,
                defaults={
                    'usd_amount': requests.get(cls.GET_CURRENCY_URL.format(
                        currency=currency,
                        date=today)
                    ).json()[0]['Rate'],
                }
            )

            cache.set(f'{currency}_{today}', obj.usd_amount, 24 * 60 * 60)
            amount_in_uzs = cache.get(f'{currency}_{today}')
        return amount_in_uzs

    class Meta:
        unique_together = (('currency', 'date'),)
