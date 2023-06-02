from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Bruno Amorim'
    })


def contato(request):
    return HttpResponse('Liga para 0800')


def sobre(request):
    return HttpResponse('Somos empresa de marca de roupa')
