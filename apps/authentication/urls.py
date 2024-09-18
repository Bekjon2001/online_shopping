
from django.urls import path
from apps.authentication import views



urlpatterns = [

    path('login_page/', views.login_page, name='login-page'),
    path('login/', views.user_login, name='user_login'),
    path('logout/',views.logout_page, name='logout-page'),
    path('register_page/', views.register_page, name='register-page'),
    path('register/', views.user_register, name='user-register'),

]

# if settings.DEBUG:
