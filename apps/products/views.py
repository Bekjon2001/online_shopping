from importlib.resources import contents

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from apps.products.models import Product


def product_list(request: WSGIRequest)-> HttpResponse:
    context ={
        'product_list': Product.objects.order_by('-pk')
    }
    return render(request=request,template_name='shop.html',context=context)

