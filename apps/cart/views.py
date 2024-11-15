from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from datetime import datetime

from apps.cart.models import Cart
from apps.coupons.models import UsedCoupon


@login_required(login_url=settings.LOGIN_URL)
def cart(request: WSGIRequest):
    user = request.user
    code = request.session.get('coupon_data', {}).get('code')
    coupon_data = request.session.get('coupon_data')

    if coupon_data:
        end_date = datetime.strptime(coupon_data['end_date'], '%Y-%m-%d').date()
    else:
        end_date = None

    now = datetime.date(datetime.now())

    if (code is not None
            and
            UsedCoupon.objects.filter(coupon__code=code, user_id=user.pk).exists()
            and now == end_date
    ):
        del request.session['coupon_data']

    queryset = Cart.objects.annotate(total_quantity=F('quantity') * F('product__price')).filter(
        user=request.user).select_related('product')

    context = {
        'user_carts': queryset,
        'cart_total_price': queryset.aggregate(Sum('total_quantity'))['total_quantity__sum']
    }

    return render(request=request, template_name='cart.html', context=context)


@login_required(login_url=settings.LOGIN_URL)
def create_cart(request: WSGIRequest, product_id: int):
    quantity = request.POST.get('cart_quantity', 1)
    obj, created = Cart.objects.get_or_create(user=request.user, product_id=product_id)
    if obj.quantity != quantity:
        obj.quantity = quantity
        obj.save()

    return redirect(request.META['HTTP_REFERER'])


def delete_cart(request: WSGIRequest, product_id: int) -> None:
    Cart.objects.filter(product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def set_cart_quantity(request, user_cart_id: int) -> None:
    if request.method == 'GET':
        return redirect('404-page')

    cart_obj = get_object_or_404(Cart, pk=user_cart_id)

    quantity = request.POST.get('user_cart_quantity', str(cart_obj.quantity))

    if quantity.isdigit() and int(quantity) <= 0:
        cart_obj.delete()
    else:
        cart_obj.quantity = quantity
        cart_obj.save()
    return redirect(request.META['HTTP_REFERER'])
