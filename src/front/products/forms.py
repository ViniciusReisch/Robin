from django import  forms
from .models import *


class Form(forms.ModelForm):
    class Meta:
        model = Alldata
        fields = '__all__'
        exclude = ['idAllData', 'store', 'price', 'changeableprice', 'installmentprice', 'changeableinstallmentprice', 'link', 'image', 'time', 'logo', 'type', 'model', 'format', 'interface', 'capacity', 'ddr', 'frequency', 'platform', 'color', 'discount', 'oldprice']

