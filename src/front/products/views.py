from django.shortcuts import render
from .models import Alldata


def index(request):
    return render(request, 'products/index.html')


def allProducts(request):
    products = Alldata.objects.all().filter
    return render(request, 'products/allProducts.html',
                  {'products': products})


def ram(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def CPU(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def HD(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font(request):
    products = Alldata.objects.all()
    return render(request, 'products/allProducts.html',
                  {'products': products})