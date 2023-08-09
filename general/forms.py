from django import forms
#from usuarios.models import Usuario
from general.models import Rubros

class RubrosForm(forms.ModelForm):
    class Meta:
        model=Rubros
        fields= "__all__"