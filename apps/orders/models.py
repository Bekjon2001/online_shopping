from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(verbose_name=_('User'),
                             to='auth.User',
                             on_delete=models.PROTECT
                             )
    # payment_method = models.ForeignKey()
    total_price = models.DecimalField(verbose_name=_('Total price'),
                                      max_digits=10,
                                      decimal_places=2
                                      )
    delivery_price = models.DecimalField(verbose_name=_('Delivery price'),
                                         max_digits=10,
                                         decimal_places=2
                                         )
    created_at = models.DateTimeField(verbose_name=_('Created At'),
                                      auto_now_add=True
                                      )
    is_paid = models.BooleanField(verbose_name=_('Is paid'),
                                  default=False
                                  )
    paid_at = models.DateTimeField(verbose_name=_('Paid at'),
                                   auto_now_add=True
                                   )
    # coupon = models.ForeignKey()
    coupon_price = models.DecimalField(verbose_name=_('Coupon price'),
                                       max_digits=10,
                                       decimal_places=2
                                       )
    coupon_code = models.CharField(verbose_name=_('Coupon code'),
                                   max_length=20
                                   )
