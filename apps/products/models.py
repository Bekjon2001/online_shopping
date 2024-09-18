from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.categories.models import Category

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('JPY', 'JPY'),
    ("UZS", "UZS"),
)


class Product(models.Model):
    title = models.CharField(verbose_name=_('Title'),
                             max_length=255
                             )
    total_rating = models.IntegerField( verbose_name=_('Total Rating'),
                                        default=0
                                        )
    comment_count = models.IntegerField(verbose_name=_('Comment Count'),
                                        default=0
                                        )
    price = models.DecimalField(verbose_name=_('Price'),
                                max_digits=5,
                                decimal_places=2,
                                default=0
                                )
    currency = models.CharField(verbose_name=_('Currency'),
                                choices=CURRENCY_CHOICES,
                                default='USD',
                                max_length=5
                                )
    short_description = models.CharField(verbose_name=_('Short description'),
                                         max_length=255
                                         )
    long_description = models.TextField()
    category = models.ForeignKey(verbose_name=_('Category'),
                                 to=Category,
                                 on_delete=models.CASCADE
                                 )
    created_at = models.DateTimeField(verbose_name=_('Created Ad'),
                                      auto_now_add=True
                                      )
    added_at = models.DateTimeField(verbose_name=_('Added at'),
                                    auto_now_add=True
                                    )