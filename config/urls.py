from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from apps.main import views

from apps.categories.views import category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home-page'),
    path('detail/', views.detail, name='detail-page'),
    path('contact/', views.contact, name='contact-page'),
    path('checkout/', views.checkout, name='checkout-page'),
    path('cart/', views.cart, name='cart-page'),
    path('shop/', views.shop, name='shop-page'),
    path('category/', category, name='category-page'),

    # ============ about urls ===========
    path('about/', include('apps.abouts.urls')),
    # ===================================

    # =========== auth urls ==========
    path('auth/', include('apps.authentication.urls')),
    # =================================

    #=========== ckeditor urls ==========
    path("__ckeditor5/", include('django_ckeditor_5.urls')),
    #====================================




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns+stack(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ??????

