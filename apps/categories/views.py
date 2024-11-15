
from django.shortcuts import render, redirect

from apps.categories.models import Category


def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)

def set_category(request, cat_id):
    if cat_id in Category.objects.values_list('pk', flat=True):
        request.session['cat_id'] = cat_id
    else:
        request.session['cat_id'] = None
    return redirect('products:product_list')

