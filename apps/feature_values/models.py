from django.db import models
from django.utils.translation import gettext_lazy as _


from apps.features.models import Feature


class FeatureValue(models.Model):
    feature = models.ForeignKey(verbose_name=_('Feature'),
                                to=Feature,
                                on_delete=models.CASCADE
                                )
    name = models.CharField(verbose_name=_('Name'),
                            max_length=100
                            )