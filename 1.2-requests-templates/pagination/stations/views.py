from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator

 
def index(request):
  return redirect(reverse('bus_stations'))

def bus_stations(request):
  with open('data-398-2018-08-30.csv', encoding='UTF-8') as csvfile:
    reader = list(csv.DictReader(csvfile))
  
  page_number = int(request.GET.get('page', 1))
  paginator = Paginator(reader, 10)
  page = paginator.get_page(page_number)
  #  print(bas_station)

  context = { 
  'bus_stations': paginator.page(page_number).object_list,
  'page': paginator.page(page_number),
  }

  return render(request, 'stations/index.html', context)
