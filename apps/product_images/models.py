from django.db import models
from django.utils.translation import gettext_lazy as _



class ProductImage(models.Model):
    product = models.ForeignKey(
        verbose_name=_('Product'),
        to='products.Product',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='products/image/%Y/%m/%d/'
    )
    ordering_number = models.PositiveSmallIntegerField(
        verbose_name=_('Ordering number'),
        default=0
    )
