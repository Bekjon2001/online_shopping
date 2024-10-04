from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models




class ProductRating(models.Model):
    product = models.ForeignKey(
        verbose_name=_('Product'),
        to='products.Product',
        related_name='ratings',
        on_delete=models.SET_NULL,
        null=True,

    )
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=User,
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        verbose_name=_('Rating'),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)])
