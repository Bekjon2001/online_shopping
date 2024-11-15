from django.urls import path

from .views import create_comment

app_name = 'comments'
urlpatterns = [
    path('create/', create_comment, name='create_comment'),
]
