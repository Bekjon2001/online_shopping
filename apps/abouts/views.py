from django.shortcuts import render

from apps.abouts.models import About


def about(request):
    context={
        'about':About.objects.last()

    }
    return render(request=request,
                  template_name= 'about.html',
                  context=context)