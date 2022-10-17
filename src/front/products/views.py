from django.shortcuts import render
from .models import Alldata
import random
# from .filters import ProductFilter


def index(request):
    promos = list(Alldata.objects.all().filter(type='Promo'))
    random_items = random.sample(promos, 5)
    return render(request, 'products/index.html',
                  {'promos': random_items})


def ssd_promo(request):
    ssds = Alldata.objects.all().filter(name='ssd', discont='1')
    return render(request, 'products/index.html',
                  {'ssds': ssds})


def allProducts(request):
    products = Alldata.objects.all().filter
    # meu_filtro = ProductFilter(request.GET, queryset=products)
    # products = meu_filtro.qs
    return render(request, 'products/allProducts.html',
                  {'products': products, 'meu_filtro': meu_filtro})


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
    products = Alldata.objects.all().filter(type='MotherBoard', ddr='DDR3')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_ddr4(request):
    products = Alldata.objects.all().filter(type='MotherBoard', ddr='DDR4')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_ddr5(request):
    products = Alldata.objects.all().filter(type='MotherBoard', ddr='DDR5')
    return render(request, 'products/allProducts.html',
                  {'products': products})


#  MOTHERBOARD SOCKET


def motherboard_socketAM4(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='AM4')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketFM2(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='FM2+')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1700(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1700')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socket1200(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='1200')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1150(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1150')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1151(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1151')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_socketLGA1155(request):
    products = Alldata.objects.all().filter(type='MotherBoard', model='LGA1155')
    return render(request, 'products/allProducts.html',
                  {'products': products})


#  MOTHERBOARD SIZE


def motherboard_ATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='ATX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_EATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='E-ATX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_MATX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='MATX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def motherboard_MiniITX(request):
    products = Alldata.objects.all().filter(type='MotherBoard', format='Mini-ITX')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# MEMORY RAM DDR


def RAM_ddr3(request):
    products = Alldata.objects.all().filter(type='RAM Memory', ddr='DDR3')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_ddr4(request):
    products = Alldata.objects.all().filter(type='RAM Memory', ddr='DDR4')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_ddr5(request):
    products = Alldata.objects.all().filter(type='RAM Memory', ddr='DDR5')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# MEMORY RAM CAPACITY


def RAM_4gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='4GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_8gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='8GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_16gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='16GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_32gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='32GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_64gb(request):
    products = Alldata.objects.all().filter(type='RAM Memory', capacity='64GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# MEMORY RAM CAPACITY


def RAM_1600mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='1600MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_3600mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='3600MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_3200mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='3200MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_1866mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='1866MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_3000mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='3000MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_2666mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='2666MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_2400mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='2400MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_6000mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='6000MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_5600mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='5600MHz')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def RAM_4800mhz(request):
    products = Alldata.objects.all().filter(type='RAM Memory', frequency='4800MHz')
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


def GPU_GT1030(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 1030')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GT610(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 610') |  Alldata.objects.all().filter(type='GPU', model='Gt 610') | Alldata.objects.all().filter(type='GPU', model='GT610')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_GT7101GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 710 1GB') | Alldata.objects.all().filter(type='GPU', model='Gt 710 1GB') | Alldata.objects.all().filter(type='GPU', model='GT 710 1gb')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_GT7102GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 710 2GB') | Alldata.objects.all().filter(type='GPU', model='Gt 710 2GB') | Alldata.objects.all().filter(type='GPU', model='GT 710 2GB') | Alldata.objects.all().filter(type='GPU', model='GT 710 2g730')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GT730(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 730 2GB') | Alldata.objects.all().filter(type='GPU', model='Gt 730 2GB') | Alldata.objects.all().filter(type='GPU', model='GT 730 2gb')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GT240(request):
    products = Alldata.objects.all().filter(type='GPU', model='GT 240')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX10502GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1050 2GB') | Alldata.objects.all().filter(type='GPU', model='GTx 1050 2GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX10503GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1050 3GB') | Alldata.objects.all().filter(type='GPU', model='GTx 1050 3GB') | Alldata.objects.all().filter(type='GPU', model='GTX 1050 3gb')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1050TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1050 TI') | Alldata.objects.all().filter(type='GPU', model='GTx 1050 TI') | Alldata.objects.all().filter(type='GPU', model='GTx 1050 ti')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1060(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1060') | Alldata.objects.all().filter(type='GPU', model='GTx 1060') | Alldata.objects.all().filter(type='GPU', model='gtx 1060')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1070(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1070')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1070TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1070 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1080(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1080')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1080TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1080 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1630(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1630')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_GTX1650(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1650')
    return render(request, 'products/allProducts.html',
                  {'products': products})



def GPU_GTX1650SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1650 SUPER')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_GTX1660(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1660') | Alldata.objects.all().filter(type='GPU', model='GTX1660') | Alldata.objects.all().filter(type='GPU', model='GTx 1660')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_GTX1660SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1660 SUPER')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX1660TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 1660 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX750TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 750TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_GTX980TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='GTX 980 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_NVS810(request):
    products = Alldata.objects.all().filter(type='GPU', model='NVS 810')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_PROW6600(request):
    products = Alldata.objects.all().filter(type='GPU', model='PRO W6600')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROP1000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P1000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROP2000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P2000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROP400(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P400')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROP4000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P4000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROP620(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO P620')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADRORTX4000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX 4000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADRORTXA2000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX A2000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADRORTXA4000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX A4000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADRORTX4500(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX 4500')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADRORTXA5000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX A5000')
    return render(request, 'products/allProducts.html',
                  {'products': products})
def GPU_QUADROT1000(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO T1000')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROT400(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO T400')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_QUADROT600(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO T600')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_R52202GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='R5 220 2GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_R52301GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='R5 230 1GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_R52302GB(request):
    products = Alldata.objects.all().filter(type='GPU', model='R5 230 2GB')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_R7240(request):
    products = Alldata.objects.all().filter(type='GPU', model='R7 240')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2060(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2060')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2060SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2060 SUPER')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2070(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2070')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2070SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2070 SUPER')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2080(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2080')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2080SUPER(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2080 SUPER')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX2080TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 2080 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3050(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3050')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3060(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3060')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3060TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3060 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3070(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3070')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3070TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3070 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3080(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3080')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3080TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3080 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3090(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3090')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RTX3090TI(request):
    products = Alldata.objects.all().filter(type='GPU', model='RTX 3090 TI')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX460(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 460')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX550(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 550')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX5500(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5500')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX5500XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5500 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX570(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 570')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX5700(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5700')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX5700XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 5700 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX580(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 580')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX590(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 590')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6400(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6400')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6400XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6400 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6600(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6600')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6600XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6600 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6650XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6650 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6700XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6700 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6750XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6750 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6800(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6800')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6800XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6800 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def GPU_RX6900XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6900 XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_RX6500XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6500XT')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_QUADRORTXA4500(request):
    products = Alldata.objects.all().filter(type='GPU', model='QUADRO RTX 4500')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def GPU_RX6950XT(request):
    products = Alldata.objects.all().filter(type='GPU', model='RX 6950 XT')
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


# SSD INTERFACE
def SSD_NVME(request):
    products = Alldata.objects.all().filter(type='SSD', interface='NVMe')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_SATA(request):
    products = Alldata.objects.all().filter(type='SSD', interface='SATA')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# SSD FORMAT
def SSD_25(request):
    products = Alldata.objects.all().filter(type='SSD', format='2.5')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_M2(request):
    products = Alldata.objects.all().filter(type='SSD', format='M.2')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_PCIe(request):
    products = Alldata.objects.all().filter(type='SSD', format='PCIe')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# SSD CAPACITY
def SSD_120GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='120')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_128GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='128')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_1TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='1TB')
    return render(request, 'products/allProducts.html',
                  {'products': products})

def SSD_240GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='240')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_250GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='250')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_256GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='256')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_2TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='2TB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_480GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='480')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_4TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='4TB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_500GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='500')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_8TB(request):
    products = Alldata.objects.all().filter(type='SSD', model='8TB')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def SSD_980GB(request):
    products = Alldata.objects.all().filter(type='SSD', model='980')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font(request):
    products = Alldata.objects.all().filter(type='Font')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_200W(request):
    products = Alldata.objects.all().filter(type='Font', model='200W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_400W(request):
    products = Alldata.objects.all().filter(type='Font', model='400W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_450W(request):
    products = Alldata.objects.all().filter(type='Font', model='450W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_500W(request):
    products = Alldata.objects.all().filter(type='Font', model='500W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_550W(request):
    products = Alldata.objects.all().filter(type='Font', model='550W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_600W(request):
    products = Alldata.objects.all().filter(type='Font', model='600W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_650W(request):
    products = Alldata.objects.all().filter(type='Font', model='650W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_700W(request):
    products = Alldata.objects.all().filter(type='Font', model='700W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_750W(request):
    products = Alldata.objects.all().filter(type='Font', model='750W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_850W(request):
    products = Alldata.objects.all().filter(type='Font', model='850W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def font_1200W(request):
    products = Alldata.objects.all().filter(type='Font', model='1200W')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet(request):
    products = Alldata.objects.all().filter(type='Cabinet')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# CABINET COLOR
def cabinet_Azul(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Azul').filter(type='Gabinete', color='Blue')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_Branco(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='White') | Alldata.objects.all().filter(type='Gabinete', color='Branco')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_Preto(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Black') | Alldata.objects.all().filter(type='Gabinete', color='Black')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_Cinza(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Cinza').filter(type='Gabinete', color='Gray').filter(type='Gabinete', color='Prata').filter(type='Gabinete', color='Silver')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_Rosa(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Pink').filter(type='Gabinete', color='Rosa')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_Verde(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Verde').filter(type='Gabinete', color='Green')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_BrancoPreto(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Branco/Preto').filter(type='Gabinete', color='White/Black').filter(type='Gabinete', color='Preto/Branco').filter(type='Gabinete', color='Black/White')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_PretoLaranja(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Preto/Laranja')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_BlackGray(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Black/Gray')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_Red(request):
    products = Alldata.objects.all().filter(type='Gabinete', color='Red').filter(type='Gabinete', color='Vermelho')
    return render(request, 'products/allProducts.html',
                  {'products': products})


# CABINET SIZE
def cabinet_fulltower(request):
    products = Alldata.objects.all().filter(type='Gabinete', model='Full-Tower')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_midtower(request):
    products = Alldata.objects.all().filter(type='Gabinete', model='Mid-Tower')
    return render(request, 'products/allProducts.html',
                  {'products': products})


def cabinet_minitower(request):
    products = Alldata.objects.all().filter(type='Gabinete', model='Mini-Tower')
    return render(request, 'products/allProducts.html',
                  {'products': products})

