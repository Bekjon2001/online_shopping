from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.comments.models import ProductComment



@receiver((post_delete,post_save),sender=ProductComment)
def comment_post_delete_or_post_save(instance,*args,**kwargs):
    instance.product.comments_count = ProductComment.objects.filter(product_id=instance.product.id).count()
    instance.product.save()

@receiver([post_save,post_delete], sender=ProductComment)
def product_rating_post_save(instance:ProductComment,**kwargs):
    instance.product.set_avg_rating()
    instance.product.save()