from django.http import HttpResponse
from django.shortcuts import render

from home.models import Service


def home(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'home/index.html', context)
