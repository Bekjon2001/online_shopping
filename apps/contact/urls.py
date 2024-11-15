from django.urls import path
from .views import create_contact,contact

app_name = 'contacts'
urlpatterns = [
    path('', contact, name='contact-page'),
    path('create/', create_contact, name='create_contact'),
]
