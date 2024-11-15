from django.contrib import messages
from django.shortcuts import redirect

from apps.coupons.models import Coupon, UsedCoupon


def check_coupon(request):
       code = request.POST.get('coupon_code')
       if code is None:
           return redirect('home-page')

       try:
           coupon = Coupon.objects.get(code=code)
       except Coupon.DoesNotExist:
           messages.error(request,'is not valid coupon')

       else:
           if UsedCoupon.objects.filter(coupon_id =coupon.pk, user_id= request.user.pk).exists():
               messages.warning(request, 'The coupon is already used')

           else:

               request.session['coupon_data']={
                   'code':code,
                   'discount_percent':float(coupon.discount_percent),
                   'end_date':coupon.end_date.isoformat(),
               }
               messages.success(request, 'is valid coupon ')



       return redirect(request.META.get('HTTP_REFERER'))