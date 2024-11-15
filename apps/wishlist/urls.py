from django.urls import path
from .views import wishlist, wishlist_create, delete_wishlist

app_name = 'wishlists'
urlpatterns = [
    path("", wishlist, name="wishlist"),
    path("create/<int:product_id>/", wishlist_create, name="wishlist_create"),
    path("delete/<int:product_id>/", delete_wishlist, name="delete_wishlist"),
]