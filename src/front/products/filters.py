import django_filters
from django_filters import CharFilter
from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='')

    class Meta:
        model = Alldata
        fields = '__all__'
        exclude = ['idAllData', 'store', 'price', 'changeableprice', 'installmentprice', 'changeableinstallmentprice', 'link', 'image', 'time', 'logo', 'type', 'model', 'format', 'interface', 'capacity', 'ddr', 'frequency', 'platform', 'color', 'discount', 'oldprice']


