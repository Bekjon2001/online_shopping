from django.db import models
from django.utils.translation import gettext_lazy as _

class Coupon(models.Model):
    code = models.CharField(verbose_name=_('Code'),
                            max_length=10,
                            unique=True
                            )