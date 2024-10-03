from django.urls import path
from apps.products.views import product_list

app_name = 'products'  # Bu yerda namespace to'g'ri

urlpatterns = [
    path('', product_list, name='product_list'),  # product_list URL ko'rsatkichini belgilash
]
