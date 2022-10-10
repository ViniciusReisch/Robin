from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allproducts/', views.allProducts, name='allproducts'),
    path('allram/', views.ram, name='allram'),
    path('allmb/', views.motherboard, name='allmb'),

    # Motherboard DDR
    path('mbddr3/', views.motherboard_ddr3, name='motherboard_ddr3'),
    path('mbddr4/', views.motherboard_ddr4, name='motherboard_ddr4'),
    path('mbddr5/', views.motherboard_ddr5, name='motherboard_ddr5'),

    # Motherboard Socket
    path('mbAM4/', views.motherboard_socketAM4, name='motherboard_socketAM4'),
    path('mbLGA1700/', views.motherboard_socketLGA1700, name='motherboard_socketLGA1700'),
    path('mbLGA1200/', views.motherboard_socket1200, name='motherboard_socket1200'),
    path('mbLGA1150/', views.motherboard_socketLGA1150, name='motherboard_socketLGA1150'),
    path('mbLGA1151/', views.motherboard_socketLGA1151, name='motherboard_socketLGA1151'),
    path('mbLGA1155/', views.motherboard_socketLGA1155, name='motherboard_socketLGA1155'),
    path('mbFM2/', views.motherboard_socketFM2, name='motherboard_socketFM2'),

    path('allhd/', views.HD, name='allhd'),
    path('allssd/', views.SSD, name='allssd'),
    path('allgpu/', views.GPU, name='allgpu'),
    path('allcpu/', views.CPU, name='allcpu'),
    path('cpuintel/', views.Intel_CPU, name='intelcpu'),
    path('apuintel/', views.Intel_APU, name='apuintel'),
    path('socketam4/', views.socket_AM4, name='am4'),
    path('socketfm2/', views.socket_FM2, name='fm2'),
    path('socketlga1150/', views.socket_LGA1150, name='lga1150'),
    path('socketlga1151/', views.socket_LGA1151, name='lga1151'),
    path('socketlga1200/', views.socket_LGA1200, name='lga1200'),
    path('socketlga1700/', views.socket_LGA1700, name='lga1700'),
    path('socketlga2066/', views.socket_LGA2066, name='lga2066'),
    path('cpuamd/', views.AMD_CPU, name='cpuamd'),
    path('apuamd/', views.AMD_APU, name='apuamd'),
    path('allfont/', views.font, name='allfont'),
    path('allcabinet/', views.cabinet, name='allcabinet'),
]