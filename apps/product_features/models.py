from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.products.models import Product
from apps.feature_values.models import FeatureValue

class ProductFeatures(models.Model):
    product = models.ForeignKey(verbose_name=_('Product'),
                                to=Product,
                                on_delete=models.CASCADE
                                )
    feature_value = models.ForeignKey(verbose_name=_('Feature value'),
                                      to=FeatureValue,
                                      on_delete=models.CASCADE
                                      )