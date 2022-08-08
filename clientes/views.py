import re
from threading import local
from django.shortcuts import render, redirect
from django.views.generic import View,ListView
from django.http import JsonResponse, HttpResponse
from .models import Clientes
from general.models import Provincias, Localidades

# Create your views here.

class ClienteHomeView(View):
    def get(self, request,*args, **kwargs):
        clientes=Clientes.objects.all()
        return render(request, 'clientes/index.html', {"clientes":clientes})
    
class CrearView(View):
    def get(self,request,*args, **kwargs):
        provincia=Provincias.objects.all()
        context={
        'provincia':provincia,
        }
        return render(request,'clientes/crear.html',context)   

    def post(self,request,*args,**kwargs):
        cliente=Clientes()
        cliente.cuil=request.POST.get('cuil')
        cliente.nombre=request.POST.get('nombre')
        cliente.direccion=request.POST.get('direccion')
        cliente.provincia=request.POST.get('provincia')
        cliente.localidad=request.POST.get('localidad')
        cliente.fecha_alta=request.POST.get('fecha_alta')
        print(cliente.cuil)
        cliente.save()
        return redirect('clientes:home')
            
def ListaLocalidades(request, id):

    loca=Localidades.objects.filter(codigo_provincia=id)
    lista_localidades=[]
    for localidad in loca:
        localidades={}
        localidades['id']=localidad.id 
        localidades['codigo_provincia']=localidad.codigo_provincia
        localidades['detalle']=localidad.nombre_localidad
        lista_localidades.append(localidades)

    return JsonResponse({"localidades":lista_localidades})

def eliminar(request, id):
    cliente=Clientes.objects.get(id=id)
    cliente.delete()
    
    return redirect('clientes:home')

def editar(request, id):
    
    cliente=Clientes.objects.get(id=id) 
    provincia=Provincias.objects.filter(id=cliente.provincia) 
    localidad=Localidades.objects.filter(codigo_provincia=cliente.provincia, codigo_localidad=cliente.localidad)   
    print(provincia)
    print(localidad)
    if request.method=="POST":
        cliente.cuil=request.POST.get('cuil')
        cliente.nombre=request.POST.get('nombre')
        cliente.direccion=request.POST.get('direccion')
        cliente.provincia=request.POST.get('provincia')
        cliente.localidad=request.POST.get('localidad')
        cliente.fecha_alta=request.POST.get('fecha_alta')
        print(cliente.cuil)
        cliente.save()
        return redirect('clientes:home')

    context = {
        'cliente':cliente,
        'provincia':provincia,
        'localidad':localidad,
    }
    return render(request, 'clientes/editar.html',context)  

def BuscarLoc(request):
    def get(self, request,*args, **kwargs):
        id=request.GET.get('id')
        localidades=list(Localidades.objects.filter(codigo_provincia=id).values)
        print(id)
        return JsonResponse(localidades)
    

