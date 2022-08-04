from asyncio.windows_events import NULL
import re
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Clientes
from .forms import ClienteForm
from general.models import Provincias, Localidades

# Create your views here.

class ClienteHomeView(View):
    def get(self, request,*args, **kwargs):
        clientes=Clientes.objects.all()
        return render(request, 'clientes/index.html', {"clientes":clientes})
    
def crear(request):
    provincias=Provincias.objects.all()
    if request.method=="POST":
        cliente=Clientes()
        cliente.cuil=request.POST.get('cuil')
        cliente.nombre=request.POST.get('nombre')
        cliente.direccion=request.POST.get('direccion')
        cliente.provincia=request.POST.get('provincia')
        if request.POST.get('localidad') == NULL:
            cliente.localidad=24
        else:
            cliente.localidad=request.POST.get('localidad')
        cliente.fecha_alta=request.POST.get('fecha_alta')
        print(cliente.cuil)
        cliente.save()
        return redirect('clientes:home')
    context={
        'provincias':provincias,
    }
    return render(request,'clientes/crear.html',context)   

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

def buscarLoc(request, id):
    localidades=Localidades.get(id)
    print(localidades)