from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .models import Proveedores
from general.models import Provincias, Localidades

# Create your views here.

class ProveedoresHomeView(View):
    def get(self, request,*args, **kwargs):
        proveedores=Proveedores.objects.all()
        proveedor=[]
        for p in proveedores:
            prov=Provincias.objects.get(id=p.provincia)
            loc=Localidades.objects.get(codigo_provincia=prov.id, codigo_localidad=p.localidad)
            pro={}
            pro['id']=p.id
            pro['cuit_cuil']=p.cuit_cuil
            pro['nombre']=p.nombre 
            pro['domicilio']=p.domicilio 
            pro['provincia']=prov.nombre
            pro['localidad']=loc.nombre_localidad
            pro['contacto']=p.contacto            
            pro['telefono']=p.telefono
            pro['email']=p.email            
            pro['observaciones']=p.observaciones
            proveedor.append(pro)
        context={
            'proveedores':proveedor,
            }
        return render(request, 'proveedores/index.html', context)
    
class CrearView(View):
    def get(self,request,*args, **kwargs):
        provincias=Provincias.objects.all()
        context={
        'provincias':provincias,
        }
        return render(request,'proveedores/crear.html',context)   

    def post(self,request,*args,**kwargs):
        proveedor=Proveedores()
        proveedor.cuit_cuil=request.POST.get('cuit_cuil')
        proveedor.nombre=request.POST.get('nombre')
        proveedor.domicilio=request.POST.get('domicilio')
        proveedor.provincia=request.POST.get('provincia')
        proveedor.localidad=request.POST.get('localidad')
        proveedor.contacto=request.POST.get('contacto')
        proveedor.telefono=request.POST.get('telefono')
        proveedor.email=request.POST.get('email')
        proveedor.observaciones=request.POST.get('observaciones')
        
        proveedor.save()
        return redirect('proveedores:home')
            
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
    proveedor=Proveedores.objects.get(id=id)
    proveedor.delete()
    
    return redirect('proveedores:home')

def editar(request, id):
    
    proveedor=Proveedores.objects.get(id=id) 
    provincia=Provincias.objects.all() 
 
    if request.method=="POST":
        proveedor.cuit_cuil=request.POST.get('cuit_cuil')
        proveedor.nombre=request.POST.get('nombre')
        proveedor.domicilio=request.POST.get('domicilio')
        proveedor.provincia=request.POST.get('provincia')
        proveedor.localidad=request.POST.get('localidad')
        proveedor.contacto=request.POST.get('contacto')
        proveedor.email=request.POST.get('email')
        proveedor.telefono=request.POST.get('telefono')
        proveedor.observaciones=request.POST.get('observaciones')
       
        proveedor.save()
        return redirect('proveedores:home')

    context = {
        'proveedores':proveedor,
        'provincias':provincia,
    }
    return render(request, 'proveedores/editar.html',context)  

