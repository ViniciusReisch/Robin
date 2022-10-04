from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allproducts/', views.allProducts, name='allproducts'),
    path('allram/', views.ram, name='allram'),
]