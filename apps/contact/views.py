from django.contrib import messages
from django.shortcuts import render, redirect

from apps.contact.forms import ContactCreateForm


def contact(request):
    return render(request=request, template_name='contact.html', context={'page': 'contact'})


def create_contact(request):
    if request.method == 'GET':
        return redirect('404-page')
    form = ContactCreateForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your message has been done!')
    else:
        messages.error(request, form.errors)


    return redirect(request.META.get('HTTP_REFERER'))
