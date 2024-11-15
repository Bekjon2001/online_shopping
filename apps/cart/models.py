from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


    class Meta:
        unique_together = (('user', 'product'),)
