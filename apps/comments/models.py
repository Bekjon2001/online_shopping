from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProductComment(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.user:
            self.name, self.email = self.user.get_full_name(), self.user.email
        super().save(*args, **kwargs)
