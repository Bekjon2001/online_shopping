from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

from apps.authentication.forms import UserRegistrationForm


def login_page(request):
    return render(request=request, template_name='auth/auth-login-basic.html')


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, email=username, password=password)
    if not user:
        messages.error(request, 'Invalid username or password.')
        return redirect(settings.LOGIN_URL)
    login(request, user)
    return redirect(settings.LOGIN_REDIRECT_URL)


def logout_page(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def register_page(request):
    form = UserRegistrationForm()
    return render(request, 'auth/auth-register-basic.html', {'form': form})


def user_register(request):
    obj_register = UserRegistrationForm(request.POST)
    if obj_register.is_valid():
        messages.success(request, 'Account was created successfully.')
        get_user_model().objects.create_user(**obj_register.cleaned_data)
    else:
        messages.error( request=request,message= obj_register.errors)
        return redirect(settings.LOGIN_REDIRECT_URL)
    return redirect(settings.LOGIN_URL)




# Create your views here.
