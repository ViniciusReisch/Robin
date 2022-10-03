from django.shortcuts import render
from .models import Alldata

def index(request):
    return render(request, 'products/index.html')

def allProducts(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})

