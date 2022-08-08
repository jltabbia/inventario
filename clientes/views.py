from threading import local
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .models import Clientes
from general.models import Provincias, Localidades
from datetime import datetime, timedelta

# Create your views here.

class ClienteHomeView(View):
    def get(self, request,*args, **kwargs):
        clientes=Clientes.objects.all()
        cliente=[]
        for c in clientes:
            pro=Provincias.objects.get(id=c.provincia)
            print(pro)
            loc=Localidades.objects.get(codigo_provincia=c.provincia, codigo_localidad=c.localidad)
            cli={}
            cli['id']=c.id
            cli['cuil']=c.cuil
            cli['nombre']=c.nombre 
            cli['direccion']=c.direccion 
            cli['provincia']=pro.nombre
            cli['localidad']=loc.nombre_localidad
            cli['fecha_alta']=c.fecha_alta
            cliente.append(cli)
        context={
            'clientes':cliente,
            }
        return render(request, 'clientes/index.html', context)
    
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
        localidades['codigo_localidad']=localidad.codigo_localidad
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
    provincia=Provincias.objects.all() 
    print(datetime.strptime(cliente.fecha_alta, "%d-%m-%Y"))
    if request.method=="POST":
        cliente.cuil=request.POST.get('cuil')
        cliente.nombre=request.POST.get('nombre')
        cliente.direccion=request.POST.get('direccion')
        cliente.provincia=request.POST.get('provincia')
        cliente.localidad=request.POST.get('localidad')
        cliente.fecha_alta=request.POST.get('fecha_alta')
       
        cliente.save()
        return redirect('clientes:home')

    context = {
        'cliente':cliente,
        'provincia':provincia,
    }
    return render(request, 'clientes/editar.html',context)  

