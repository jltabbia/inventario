from django import forms 
from .models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['cuil','nombre','direccion','fecha_alta','localidad','provincia','estado']