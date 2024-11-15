from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


from apps.wishlist.models import Wishlist


@receiver((post_delete,post_save), sender=Wishlist)
def wishlist_post_delete_or_save(instance, **kwargs):
    instance.user.user_wishlist_count = Wishlist.objects.filter(user_id=instance.user_id).count()
    instance.user.save()