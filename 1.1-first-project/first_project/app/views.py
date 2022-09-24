from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime as dt
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir_view'),

    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    current_time = dt.datetime.now().strftime('%H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    listdir = [dir_+' ' for dir_ in os.listdir()]
    return HttpResponse(listdir)
    raise NotImplemented
