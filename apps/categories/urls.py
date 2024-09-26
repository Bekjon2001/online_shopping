from django.urls import path
from apps.categories.views import category

urlpatterns = [

    # ============ about urls ===========
    path('',category, name='category-page'),
    # ===================================


]