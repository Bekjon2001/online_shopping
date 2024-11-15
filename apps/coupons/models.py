from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Coupon(models.Model):
    title = models.CharField(max_length=120)
    code = models.CharField(max_length=10, unique=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    discount_percent = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )



    def __str__(self):
        return self.title

class UsedCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

