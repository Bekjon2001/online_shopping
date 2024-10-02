from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.products.models import Product


class ProductRating(models.Model):
    product = models.ForeignKey(
        verbose_name=_('Product'),
                                to=Product,
                                on_delete=models.CASCADE
                                )
    user = models.ForeignKey(
        verbose_name=_('User'),
                             to=User,
                             on_delete=models.CASCADE
                             )
    rating = models.IntegerField(
        verbose_name=_('Rating'),
                                 default=0,
                                 validators=[MinValueValidator(1), MaxValueValidator(5)])