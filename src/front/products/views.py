from django.shortcuts import render
from .models import Alldata
import random
from .filters import ProductFilter


def index(request):
    promos = Alldata.objects.all().filter(type='Promo')
    ssds = promos.filter(name__contains='SSD')
    rams = promos.filter(name__contains='RAM')
    random_items = random.sample(list(promos), 5)
    random_ssds = random.sample(list(ssds), 5)
    random_rams = random.sample(list(ssds), 3)
    return render(request, 'products/index.html',
                  {'promos': random_items, 'ssds': random_ssds, 'rams': random_rams})


def allProducts(request):
    products = Alldata.objects.all()
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def low_price(request):
    products = Alldata.objects.all().order_by('price')
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def ram(request):
    products = Alldata.objects.all().filter(type='RAM Memory')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def motherboard(request):
    products = Alldata.objects.all().filter(type='MotherBoard')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


#  MOTHERBOARD DDR


def motherboard_ddr3(request):
    products = Alldata.objects.all().filter(type='MotherBoard', ddr='DDR3')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_ddr4(request):
    products = Alldata.objects.all().filter(type='MotherBoard', ddr='DDR4')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def motherboard_ddr5(request):
    products = Alldata.objects.all().filter(type='MotherBoard', ddr='DDR5')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


#  MOTHERBOARD SOCKET


def motherboard_socketAM4(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='AM4')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_socketFM2(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='FM2+')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def motherboard_socketLGA1700(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1700')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_socket1200(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='1200')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_socketLGA1150(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1150')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_socketLGA1151(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1151')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def motherboard_socketLGA1155(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1155')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


#  MOTHERBOARD SIZE


def motherboard_ATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='ATX')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_EATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='E-ATX')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_MATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='MATX')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def motherboard_MiniITX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='Mini-ITX')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# MEMORY RAM DDR


def RAM_ddr3(request):
    products = Alldata.objects.all().filter(type='RAM Memory', ddr='DDR3')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_ddr4(request):
    products = Alldata.objects.all().filter(type='RAM Memory', ddr='DDR4')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_ddr5(request):
    products = Alldata.objects.all().filter(type='RAM Memory', ddr='DDR5')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# MEMORY RAM CAPACITY


def RAM_4gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='4GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_8gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='8GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_16gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='16GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_32gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='32GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_64gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='64GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

# MEMORY RAM CAPACITY


def RAM_1600mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='1600MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_3600mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='3600MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_3200mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='3200MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_1866mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='1866MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_3000mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='3000MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_2666mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='2666MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_2400mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='2400MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_6000mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='6000MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_5600mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='5600MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def RAM_4800mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='4800MHz')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def CPU(request):
    products = Alldata.objects.all().filter(type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def Intel_CPU(request):
    products = Alldata.objects.all().filter(platform='Intel CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def AMD_CPU(request):
    products = Alldata.objects.all().filter(platform='AMD CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def Intel_APU(request):
    products = Alldata.objects.all().filter(platform='Intel APU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def AMD_APU(request):
    products = Alldata.objects.all().filter(platform='AMD APU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_AM4(request):
    products = Alldata.objects.all().filter(model='AM4', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_FM2(request):
    products = Alldata.objects.all().filter(model='FM2+', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_LGA1150(request):
    products = Alldata.objects.all().filter(model='LGA1150', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_LGA1151(request):
    products = Alldata.objects.all().filter(model='LGA1151', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_LGA1200(request):
    products = Alldata.objects.all().filter(model='LGA1200', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_LGA1700(request):
    products = Alldata.objects.all().filter(model='LGA1700', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def socket_LGA2066(request):
    products = Alldata.objects.all().filter(model='LGA2066', type='CPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU(request):
    products = Alldata.objects.all().filter(type='GPU')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GT1030(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 1030')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GT610(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 610') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='Gt 610') | Alldata.objects.all().filter(
        type='GPU', model='GT610')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GT7101GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 710 1GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Gt 710 1GB') | Alldata.objects.all().filter(
        type='GPU', model='GT 710 1gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GT7102GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 710 2GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Gt 710 2GB') | Alldata.objects.all().filter(
        type='GPU', model='GT 710 2GB') | Alldata.objects.all().filter(type='GPU', model='GT 710 2g730')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GT730(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 730 2GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Gt 730 2GB') | Alldata.objects.all().filter(
        type='GPU', model='GT 730 2gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GT240(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 240')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX10502GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1050 2GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                             model='GTx 1050 2GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX10503GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1050 3GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                             model='GTx 1050 3GB') | Alldata.objects.all().filter(
        type='GPU', model='GTX 1050 3gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1050TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1050 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='GTx 1050 TI') | Alldata.objects.all().filter(
        type='GPU', model='GTx 1050 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1060(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1060') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='GTx 1060') | Alldata.objects.all().filter(
        type='GPU', model='gtx 1060') | Alldata.objects.all().filter(type='GPU', model='GTX 1060 3GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1070(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1070') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='GTx 1070')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1070TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1070 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='GTx 1070 TI') | Alldata.objects.all().filter(
        type='GPU', model='GTX 1070 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1080(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1080') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='GTx 1080')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1080TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1080 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='GTx 1080 TI') | Alldata.objects.all().filter(
        type='GPU', model='GTX 1080 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1630(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1630') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='GTx 1630')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1650(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1650') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='GTx 1650')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX16504GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1650 4GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                             model='Gtx 1650 4GB') | Alldata.objects.all().filter(
        type='GPU', model='GTX 1650 4gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1650SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1650 SUPER')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1660(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1660') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='GTX1660') | Alldata.objects.all().filter(
        type='GPU', model='GTx 1660')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1660SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1660 SUPER')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX1660TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1660 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='Gtx 1660 TI')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX750TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 750TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                          model='GTX 750TI,2GB') | Alldata.objects.all().filter(
        type='GPU', model='GTX 750TI,4GB') | Alldata.objects.all().filter(type='GPU',
                                                                          model='GTx 750TI,2GB') | Alldata.objects.all().filter(
        type='GPU', model='GTX 750ti,2GB') | Alldata.objects.all().filter(type='GPU',
                                                                          model='GTX 750TI 2gb') | Alldata.objects.all().filter(
        type='GPU', model='GTX 750TI') | Alldata.objects.all().filter(type='GPU', model='GTX 750TI 2gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_GTX980TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 980 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='GTx 980 TI') | Alldata.objects.all().filter(
        type='GPU', model='GTX 980 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_NVS810(request):
    products = Alldata.objects.all().filter(type='GPU', model='NVS 810')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_PROW6600(request):
    products = Alldata.objects.all().filter(type='GPU', model='PRO W6600')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROP1000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P1000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROP2000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P2000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROP400(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P400')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROP4000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P4000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROP620(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P620')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADRORTX4000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX 4000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADRORTXA2000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX A2000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADRORTXA4000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX A4000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADRORTX4500(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX 4500')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADRORTXA5000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX A5000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROT1000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO T1000')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROT400(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO T400')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADROT600(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO T600')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_R52202GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='R5 220 2GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_R52301GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='R5 230 1GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='R5 230 1gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_R52302GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='R5 230 2GB') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='R5 230 2gb')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_R7240(request):
    products = Alldata.objects.all().filter(type='GPU', model='R7 240') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='R7 240 2GB') | Alldata.objects.all().filter(
        type='GPU', model='R7 240 2gb') | Alldata.objects.all().filter(type='GPU', model='R7 240,2GB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2060(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2060') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 2060') | Alldata.objects.all().filter(
        type='GPU', model='RTx 2060')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2060SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2060 SUPER') | Alldata.objects.all().filter(
        type='GPU', model='Rtx 2060 SUPER') | Alldata.objects.all().filter(type='GPU', model='RTx 2060 SUPER')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2070(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2070') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 2070') | Alldata.objects.all().filter(
        type='GPU', model='RTx 2070')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2070SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2070 Super') | Alldata.objects.all().filter(
        type='GPU', model='Rtx 2070 SUPER') | Alldata.objects.all().filter(type='GPU',
                                                                           model='RTx 2070 SUPER') | Alldata.objects.all().filter(
        type='GPU', model='RTX 2070 SUPER')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2080(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2080') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 2080') | Alldata.objects.all().filter(
        type='GPU', model='RTx 2080')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2080SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2080 Super') | Alldata.objects.all().filter(
        type='GPU', model='Rtx 2080 Super') | Alldata.objects.all().filter(type='GPU',
                                                                           model='RTx 2080 Super') | Alldata.objects.all().filter(
        type='GPU', model='RTX 2080 SUPER')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX2080TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2080 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='Rtx 2080 TI') | Alldata.objects.all().filter(
        type='GPU', model='RTx 2080 TI') | Alldata.objects.all().filter(type='GPU', model='RTX 2080 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3050(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3050') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='RTx 3050') | Alldata.objects.all().filter(
        type='GPU', model='Rtx 3050')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3060(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3060') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 3060') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3060')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3060TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3060 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='Rtx 3060 TI') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3060 TI') | Alldata.objects.all().filter(type='GPU', model='RTX 3060 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3070(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3070') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 3070') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3070')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3070TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3070 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='Rtx 3070 TI') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3070 TI') | Alldata.objects.all().filter(type='GPU', model='RTX 3070 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3080(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3080') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 3080') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3080')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3080TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3080 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='Rtx 3080 TI') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3080 TI') | Alldata.objects.all().filter(type='GPU', model='RTX 3080 ti')

    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def GPU_RTX3090(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3090') | Alldata.objects.all().filter(type='GPU',
                                                                                                         model='Rtx 3090') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3090')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RTX3090TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3090 TI') | Alldata.objects.all().filter(type='GPU',
                                                                                                            model='Rtx 3090 TI') | Alldata.objects.all().filter(
        type='GPU', model='RTx 3090 TI') | Alldata.objects.all().filter(type='GPU', model='RTX 3090 ti')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX460(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 460') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='Rx 460')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX550(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 550') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='Rx 550')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def GPU_RX5500(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5500') | Alldata.objects.all().filter(type='GPU',
                                                                                                        model='Rx 5500')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX5500XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5500 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 5500 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 5500 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 5500 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX570(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 570') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='Rx 570')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX5700(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5700') | Alldata.objects.all().filter(type='GPU',
                                                                                                        model='RX 5700')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX5700XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5700 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 5700 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 5700 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 5700 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX580(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 580') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='Rx 580')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX590(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 590') | Alldata.objects.all().filter(type='GPU',
                                                                                                       model='Rx 590')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6400(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6400') | Alldata.objects.all().filter(type='GPU',
                                                                                                        model='Rx 6400')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6400XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6400 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6400 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6400 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6400 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6600(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6600') | Alldata.objects.all().filter(type='GPU',
                                                                                                        model='RX 6600')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6600XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6600 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6600 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6600 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6600 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6650XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6650 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6650 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6650 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6650 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6700XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6700 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6700 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6700 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6700 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6750XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6750 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6750 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6750 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6750 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6800(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6800') | Alldata.objects.all().filter(type='GPU',
                                                                                                        model='Rx 6800')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6800XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6800 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6800 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6800 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6800 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6900XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6900 XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                           model='Rx 6900 XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6900 xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6900 Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6500XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6500XT') | Alldata.objects.all().filter(type='GPU',
                                                                                                          model='Rx 6500XT') | Alldata.objects.all().filter(
        type='GPU', model='RX 6500xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6500Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_QUADRORTXA4500(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX 4500')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def GPU_RX6950XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6950 XT') | Alldata.objects.all().filter(type='GPU', model='Rx 6950 XT') | \
               Alldata.objects.all().filter(type='GPU', model='RX 6950 xt') | Alldata.objects.all().filter(type='GPU',model='Rx 6950 Xt') | \
               Alldata.objects.all().filter(type='GPU', model='RX 6950XT') | Alldata.objects.all().filter(type='GPU',model='Rx 6950XT') | \
               Alldata.objects.all().filter(type='GPU', model='RX 6950xt') | Alldata.objects.all().filter(type='GPU', model='Rx 6950Xt')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD(request):
    products = Alldata.objects.all().filter(type='HardDisk')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_10TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='10TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_12TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='12TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_14TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='14TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_16TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='16TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_1TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='1TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_2TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='2TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_3TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='3TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_4TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='4TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_6TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='6TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def HD_8TB(request):
    products = Alldata.objects.all().filter(type='HardDisk', model='8TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD(request):
    products = Alldata.objects.all().filter(type='SSD')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# SSD INTERFACE
def SSD_NVME(request):
    products = Alldata.objects.all().filter(type='SSD', interface='NVMe')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_SATA(request):
    products = Alldata.objects.all().filter(type='SSD', interface='SATA')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# SSD FORMAT
def SSD_25(request):
    products = Alldata.objects.all().filter(type='SSD', format='2.5')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_M2(request):
    products = Alldata.objects.all().filter(type='SSD', format='M.2')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_PCIe(request):
    products = Alldata.objects.all().filter(type='SSD', format='PCIe')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# SSD CAPACITY
def SSD_120GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='120')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_128GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='128')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_1TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='1TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_240GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='240')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_250GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='250')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_256GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='256')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_2TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='2TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})

def SSD_480GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='480')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_4TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='4TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_500GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='500')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_8TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='8TB')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def SSD_980GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='980')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font(request):
    products = Alldata.objects.all().filter(type='Font')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_200W(request):
    products = Alldata.objects.all().filter(type='Font', model='200W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_400W(request):
    products = Alldata.objects.all().filter(type='Font', model='400W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_450W(request):
    products = Alldata.objects.all().filter(type='Font', model='450W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_500W(request):
    products = Alldata.objects.all().filter(type='Font', model='500W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_550W(request):
    products = Alldata.objects.all().filter(type='Font', model='550W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_600W(request):
    products = Alldata.objects.all().filter(type='Font', model='600W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_650W(request):
    products = Alldata.objects.all().filter(type='Font', model='650W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_700W(request):
    products = Alldata.objects.all().filter(type='Font', model='700W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_750W(request):
    products = Alldata.objects.all().filter(type='Font', model='750W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_850W(request):
    products = Alldata.objects.all().filter(type='Font', model='850W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def font_1200W(request):
    products = Alldata.objects.all().filter(type='Font', model='1200W')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet(request):
    products = Alldata.objects.all().filter(type='Cabinet')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# CABINET COLOR
def cabinet_Azul(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Azul').filter(type='Gabinete', color='Blue')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_Branco(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='White') | Alldata.objects.all().filter(type='Gabinete', color='Branco')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_Preto(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Black') | Alldata.objects.all().filter(
        type='Gabinete', color='Black')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_Cinza(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Cinza').filter(type='Gabinete',
                                                                                   color='Gray').filter(type='Gabinete',
                                                                                                        color='Prata').filter(
        type='Gabinete', color='Silver')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_Rosa(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Pink').filter(type='Gabinete', color='Rosa')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_Verde(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Verde').filter(type='Gabinete', color='Green')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_BrancoPreto(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Branco/Preto').filter(type='Gabinete',
                                                                                          color='White/Black').filter(
        type='Gabinete', color='Preto/Branco').filter(type='Gabinete', color='Black/White')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_PretoLaranja(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Preto/Laranja')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_BlackGray(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Black/Gray')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_Red(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Red').filter(type='Gabinete', color='Vermelho')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


# CABINET SIZE
def cabinet_fulltower(request):
    products = Alldata.objects.all().filter(type='Gabinete', model='Full-Tower')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_midtower(request):
    products = Alldata.objects.all().filter(type='Gabinete', model='Mid-Tower')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})


def cabinet_minitower(request):
    products = Alldata.objects.all().filter(type='Gabinete', model='Mini-Tower')
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'my_filter': my_filter})
