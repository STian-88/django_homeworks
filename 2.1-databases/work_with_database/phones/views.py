from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_list = Phone.objects.all()
    if request.GET.get('sort') == 'name':
        phones_list = Phone.objects.all().order_by('-name')
    if request.GET.get('sort') == 'min_price':
        phones_list = Phone.objects.all().order_by('price')
    if request.GET.get('sort') == 'max_price':
        phones_list = Phone.objects.all().order_by('-price')
    context = {'phones': phones_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    slug =' '.join(slug.split('-')) 
    phone = Phone.objects.get(name__iexact=slug)
    print(slug)
    print(phone)
    context = {'phone': phone
    }
    return render(request, template, context)
