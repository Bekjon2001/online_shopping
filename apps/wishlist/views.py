
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from apps.wishlist.models import Wishlist


def wishlist(request: WSGIRequest):
    if not request.user.is_authenticated:
        return redirect('login-page')
    context = {
        'wishlists': Wishlist.objects.filter(user=request.user).select_related('product')
    }
    return render(request=request, template_name='wishlist.html', context=context)


@login_required(login_url='login-page')
def wishlist_create(request: WSGIRequest, product_id: int):
    Wishlist.objects.get_or_create(product_id=product_id, user=request.user)
    return redirect(request.META['HTTP_REFERER'])


def delete_wishlist(request: WSGIRequest, product_id: int) -> None:
    Wishlist.objects.filter(product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])
