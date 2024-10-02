from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.products.models import Product


class Product_image(models.Model):
    product = models.ForeignKey(
        verbose_name=_('Product'),
        to=Product,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='product_images/image/%Y/%m/%d/'
    )
    ordering_number = models.PositiveSmallIntegerField(
        verbose_name=_('Ordering number'),
        default=0
    )
