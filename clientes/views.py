import re
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Clientes
from .forms import ClienteForm

# Create your views here.

class ClienteHomeView(View):
    def get(self, request,*args, **kwargs):
        clientes=Clientes.objects.all()
        return render(request, 'clientes/index.html', {"clientes":clientes})
    
def crear(request):
        formulario=ClienteForm(request.POST or None)  
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes:home')
        return render(request,'clientes/crear.html',{'formulario':formulario})   

def eliminar(request, id):
    cliente=Clientes.objects.get(id=id)
    cliente.delete()
    
    return redirect('clientes:home')

def editar(request, id):
    cliente=Clientes.objects.get(id=id) 
    formulario=ClienteForm(request.POST or None, instance=cliente)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes:home')
    
    return render(request, 'clientes/editar.html',{'formulario':formulario})  