from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


from apps.cart.models import Cart


@receiver((post_delete,post_save), sender=Cart)
def cart_post_delete_or_save(instance, **kwargs):
    quantity_sum = Cart.objects.filter(user_id=instance.user_id).aggregate(total_quantity=Sum('quantity'))[
                       'total_quantity'] or 0
    instance.user.user_cart_count = quantity_sum
    instance.user.save()
    print(instance.user.user_cart_count)