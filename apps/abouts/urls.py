from django.urls import path
from apps.abouts.views import about



urlpatterns = [

    # ============ about urls ===========
    path('',about, name='about-page'),
    # ===================================


]