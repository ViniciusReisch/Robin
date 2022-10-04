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
    path('allfont/', views.font, name='allfont'),
    path('allcabinet/', views.cabinet, name='allcabinet'),
]