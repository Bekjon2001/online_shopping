from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from apps.general.views import (
    set_language,
    home,
    checkout,
    search,
    set_currency,
    page_404,
    clear_session,
)

urlpatterns = [
    # =========== CKEDITOR URLS  ============
    path("__ckeditor5/", include('django_ckeditor_5.urls')),

    # =============MEDIA URLS===========
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    # =======SET LANGUAGE URLS =======
    path('set-language/<str:lang>/', set_language, name='set-lang'),

    # =======SET CURRENCY URLS =======
    path('set-currency/<str:currency>/', set_currency, name='set-currency'),
]
urlpatterns += i18n_patterns(
    path('', home, name='home-page'),
    path('admin/', admin.site.urls),

    # ======= General URLS =======

    path('checkout/', checkout, name='checkout-page'),
    path('search/', search, name='search'),
    path('clear-session/', clear_session, name='clear_session'),


    # ============= CATEGORIES URLS =============
    path('category/', include('apps.categories.urls', namespace='categories')),

    # ============= CONTACT URLS =============
    path('contact/', include('apps.contact.urls', namespace='contacts')),

    # ============= ABOUT URLS =============
    path('about/', include('apps.abouts.urls', namespace='about')),

    # ============= WISHLIST URLS =============
    path('wishlist/', include('apps.wishlist.urls', namespace='wishlists')),

    # ============= CART URLS =============
    path('cart/', include('apps.cart.urls', namespace='carts')),

    # ============= COUPONS URLS =============
    path('coupons', include('apps.coupons.urls', namespace='coupons')),

    # =============  PRODUCTS URLS =============
    path('products/', include('apps.products.urls', namespace='products')),

    # =============  COMMENTS URLS =============
    path('comments/', include('apps.comments.urls', namespace='comments')),

    # ============= AUTH URLS  =============
    path('auth/', include('apps.authentication.urls')),

    # ============= DEBUG_TOOLBAR URLs =============
    path('__debug__/', include('debug_toolbar.urls')),

    # ============= 404 URLS =============
    path('404/', page_404, name='404-page'),

)
