from django.conf import settings
from django.db import models


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(to='products.product', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'product'),)


