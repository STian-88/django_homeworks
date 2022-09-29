from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator

with open('data-398-2018-08-30.csv', encoding='UTF-8') as csvfile:
  reader = csv.DictReader(csvfile)
 
def index(request):
  return redirect(reverse('bus_stations'))

def bus_stations(request):
  page_number = int(request.GET.get('page', 1))
  paginator = paginator(reader, 10)
  page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

  context = {
    #     'bus_stations': ...,
         'page': page,
    }
  return render(request, 'stations/index.html', context)
