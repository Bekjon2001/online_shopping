from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, EmailField
from django.utils.translation import gettext_lazy as _

from apps.products.models import Product


class ProductComment(models.Model):
    product = models.ForeignKey(verbose_name=_('Product'),
                                to=Product,
                                on_delete=models.CASCADE
                                )
    user = models.ForeignKey(verbose_name=_('User') ,
                             to=User,
                             on_delete=models.CASCADE
                             )
    name = CharField(verbose_name=_('Name'),
                     max_length=120
                     )
    email = EmailField(max_length=120)
    message = models.CharField(verbose_name=_('Message'),
                               max_length=250
                               )
    created_at = models.DateTimeField(verbose_name=_('Created At'),
                                      auto_now_add=True
                                      )
