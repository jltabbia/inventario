import re
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Inventario
from .forms import InventarioForm

# Create your views here.

class InventarioHomeView(View):
    def get(self, request,*args, **kwargs):
        inventario=Inventario.objects.all()
        return render(request, 'inventario/index.html', {"inventario":inventario})
    
def crear(request):
        formulario=InventarioForm(request.POST or None)  
        if formulario.is_valid():
            formulario.save()
            return redirect('inventario:home')
        return render(request,'inventario/crear.html',{'formulario':formulario})   

def eliminar(request, id):
    producto=Inventario.objects.get(id=id)
    producto.delete()
    
    return redirect('inventario:home')

def editar(request, id):
    inventario=Inventario.objects.get(id=id) 
    formulario=InventarioForm(request.POST or None, instance=inventario)
    return render(request, 'inventario/editar.html',{'formulario':formulario})  