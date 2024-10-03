from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns,set_language
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.main import views
from apps.generals.views import set_language

urlpatterns = [
    # =========== ckeditor urls ==========
    path("__ckeditor5/", include('django_ckeditor_5.urls')),

    # ============ set lang ==========
    path('set-language/<str:lang>', set_language, name='set-lang'),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
urlpatterns += i18n_patterns(

    path('', views.home, name='home-page'),
    path('admin/', admin.site.urls),
    path('detail/', views.detail, name='detail-page'),
    path('contact/', views.contact, name='contact-page'),
    path('checkout/', views.checkout, name='checkout-page'),
    path('cart/', views.cart, name='cart-page'),
    path('products/', include('apps.products.urls'), name='shop-page'),
    # ============ category urls ==========
    path('category/', include('apps.categories.urls')),

    # ============ about urls ===========
    path('about/', include('apps.abouts.urls')),

    # =========== auth urls ==========
    path('auth/', include('apps.authentication.urls')),

)
