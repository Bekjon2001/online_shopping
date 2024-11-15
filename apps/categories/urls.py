from django.urls import path

from apps.categories.views import category, set_category

app_name = 'categories'
urlpatterns = [
    path('', category, name='category'),
    path('set-category/<int:cat_id>/', set_category, name='set_category'),
]
