from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ALL PATHS
    path('allproducts/', views.allProducts, name='allproducts'),
    path('allram/', views.ram, name='allram'),
    path('allmb/', views.motherboard, name='allmb'),
    path('allhd/', views.HD, name='allhd'),
    path('allssd/', views.SSD, name='allssd'),
    path('allgpu/', views.GPU, name='allgpu'),
    path('allcpu/', views.CPU, name='allcpu'),
    path('allfont/', views.font, name='allfont'),
    path('allcabinet/', views.cabinet, name='allcabinet'),


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

    # Motherboard Socket
    path('mbatx/', views.motherboard_ATX, name='motherboard_ATX'),
    path('mbeatx/', views.motherboard_EATX, name='motherboard_EATX'),
    path('mbmatx/', views.motherboard_MATX, name='motherboard_MATX'),
    path('mbminiitx/', views.motherboard_MiniITX, name='motherboard_MiniITX'),


    # CPU Format
    path('cpuintel/', views.Intel_CPU, name='intelcpu'),
    path('apuintel/', views.Intel_APU, name='apuintel'),
    path('cpuamd/', views.AMD_CPU, name='cpuamd'),
    path('apuamd/', views.AMD_APU, name='apuamd'),

    # CPU Socket
    path('socketam4/', views.socket_AM4, name='am4'),
    path('socketfm2/', views.socket_FM2, name='fm2'),
    path('socketlga1150/', views.socket_LGA1150, name='lga1150'),
    path('socketlga1151/', views.socket_LGA1151, name='lga1151'),
    path('socketlga1200/', views.socket_LGA1200, name='lga1200'),
    path('socketlga1700/', views.socket_LGA1700, name='lga1700'),
    path('socketlga2066/', views.socket_LGA2066, name='lga2066'),


    # RAM DDR

    path('ramddr3/', views.RAM_ddr3, name='RAM_ddr3'),
    path('ramddr4/', views.RAM_ddr4, name='RAM_ddr4'),
    path('ramddr5/', views.RAM_ddr5, name='RAM_ddr5'),

    # RAM Capacity

    path('ram4gb/', views.RAM_4gb, name='RAM_4gb'),
    path('ram8gb/', views.RAM_8gb, name='RAM_8gb'),
    path('ram16gb/', views.RAM_16gb, name='RAM_16gb'),
    path('ram32gb/', views.RAM_32gb, name='RAM_32gb'),
    path('ram64gb/', views.RAM_64gb, name='RAM_64gb'),

    # RAM Frequency

    path('ram1866mhz/', views.RAM_1866mhz, name='RAM_1866mhz'),
    path('ram3600mhz/', views.RAM_3600mhz, name='RAM_3600mhz'),
    path('ram3200mhz/', views.RAM_3200mhz, name='RAM_3200mhz'),
    path('ram3000mhz/', views.RAM_3000mhz, name='RAM_3000mhz'),
    path('ram2666mhz/', views.RAM_2666mhz, name='RAM_2666mhz'),
    path('ram1600mhz/', views.RAM_1600mhz, name='RAM_1600mhz'),
    path('ram2400mhz/', views.RAM_2400mhz, name='RAM_2400mhz'),
    path('ram6000mhz/', views.RAM_6000mhz, name='RAM_6000mhz'),
    path('ram5600mhz/', views.RAM_5600mhz, name='RAM_5600mhz'),
    path('ram4800mhz/', views.RAM_4800mhz, name='RAM_4800mhz'),
]