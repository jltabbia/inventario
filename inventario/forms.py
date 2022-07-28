from django import forms 
from .models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['codigo', 'detalle', 'stock', 'stock_minimo', 'ultima_compra', 'observaciones']