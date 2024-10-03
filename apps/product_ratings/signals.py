from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.product_ratings.models import ProductRating


@receiver(signal=post_save,sender=ProductRating)
def product_rating_post_sev(instance: ProductRating,**kwargs):
    instance.product.set_avg_rating()

