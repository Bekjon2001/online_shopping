from django.contrib import admin

from apps.wishlist.models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass