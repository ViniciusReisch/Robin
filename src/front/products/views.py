from django.shortcuts import render
from .models import Alldata


def index(request):
    return render(request, 'products/index.html')


def allProducts(request):
    products = Alldata.objects.all().filter
    return render(request, 'products/allProducts.html',
                  {'products': products})


def ram(request):
    products = Alldata.objects.all().filter(type='RAM Memory')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard(request):
    products = Alldata.objects.all().filter(type='MotherBoard')
    return render(request, 'products/allProducts.html',
                  {'products': products})


#  MOTHERBOARD DDR


def motherboard_ddr3(request):
    products = Alldata.objects.all().filter(type='MotherBoard', DDR='DDR3')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_ddr4(request):
    products = Alldata.objects.all().filter(type='MotherBoard', DDR='DDR4')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_ddr5(request):
    products = Alldata.objects.all().filter(type='MotherBoard', DDR='DDR5')
    return render(request, 'products/allProducts.html',
                  {'products': products})


#  MOTHERBOARD SOCKET


def motherboard_socketAM4(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='AM4')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketFM2(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='FM2+')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1700(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='LGA1700')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socket1200(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='1200')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1150(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='LGA1150')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1151(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='LGA1151')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1155(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Model='LGA1155')
    return render(request, 'products/allProducts.html',
                  {'products': products})


#  MOTHERBOARD SIZE


def motherboard_ATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Format='ATX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_EATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Format='E-ATX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_MATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Format='MATX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_MiniITX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', Format='Mini-ITX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet(request):
    products = Alldata.objects.all().filter(type='Gabinete')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def CPU(request):
    products = Alldata.objects.all().filter(type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def Intel_CPU(request):
    products = Alldata.objects.all().filter(platform='Intel CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def AMD_CPU(request):
    products = Alldata.objects.all().filter(platform='AMD CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def Intel_APU(request):
    products = Alldata.objects.all().filter(platform='Intel APU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def AMD_APU(request):
    products = Alldata.objects.all().filter(platform='AMD APU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_AM4(request):
    products = Alldata.objects.all().filter(model='AM4', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_FM2(request):
    products = Alldata.objects.all().filter(model='FM2+', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_LGA1150(request):
    products = Alldata.objects.all().filter(model='LGA1150', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_LGA1151(request):
    products = Alldata.objects.all().filter(model='LGA1151', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_LGA1200(request):
    products = Alldata.objects.all().filter(model='LGA1200', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_LGA1700(request):
    products = Alldata.objects.all().filter(model='LGA1700', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def socket_LGA2066(request):
    products = Alldata.objects.all().filter(model='LGA2066', type='CPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU(request):
    products = Alldata.objects.all().filter(type='GPU')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def HD(request):
    products = Alldata.objects.all().filter(type='HardDisk')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD(request):
    products = Alldata.objects.all().filter(type='SSD')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font(request):
    products = Alldata.objects.all().filter(type='Font')
    return render(request, 'products/allProducts.html',
                  {'products': products})