from decimal import Decimal

from django import template

from apps.general.models import CurrencyAmount, General
from apps.wishlist.models import Wishlist

register = template.Library()


@register.simple_tag
def decimal_to_range(decimal_number):
    return range(int(decimal_number))


@register.simple_tag
def product_in_wishlist(user: int, product_id: int) -> bool:
    return Wishlist.objects.filter(user=user, product_id=product_id).exists()


@register.simple_tag
def get_price_by_currency(to_currency: str, price: Decimal = 0) -> Decimal:
    if to_currency == General.Currency.UZS:
        return price
    return round(price / Decimal(CurrencyAmount.get_amount(currency=to_currency)), 2)


@register.simple_tag
def multiply(a, b):
    a = (a / 100)
    return round(a * b, 2)


@register.simple_tag
def total_cal(value1, value2):
    return value1 + value2


@register.simple_tag
def str_to_decimal(value):
    print(type(value))
    try:
        return Decimal(value)
    except (ValueError, TypeError):
        return None


@register.simple_tag
def int_to_decimal(value):
    try:
        return Decimal(value)
    except (ValueError, TypeError):
        return None
