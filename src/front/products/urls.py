from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allproducts/', views.allProducts, name='allproducts'),
    path('allram/', views.ram, name='allram'),
    path('allmb/', views.motherboard, name='allmb'),
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