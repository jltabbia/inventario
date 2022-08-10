import re
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Inventario
from .forms import InventarioForm
import datetime

# Create your views here.

class InventarioHomeView(View):
    def get(self, request,*args, **kwargs):
        inventario=Inventario.objects.all()
        return render(request, 'inventario/index.html', {"inventario":inventario})

class CrearView(View):
    def get(self,request,*args, **kwargs):
        inventario=Inventario.objects.all()
        context={
        'inventario':inventario,
        }
        return render(request,'inventario/crear.html',context)   

    def post(self,request,*args,**kwargs):
        inventario=Inventario()
        inventario.codigo=request.POST.get('codigo')
        inventario.detalle=request.POST.get('detalle')
        inventario.stock=request.POST.get('stock')
        inventario.stock_minimo=request.POST.get('stock_minimo')
        inventario.ultima_compra=request.POST.get('ultima_compra')
        inventario.observaciones=request.POST.get('observaciones')
        inventario.save()
        return redirect('inventario:home')
        
def eliminar(request, id):
    producto=Inventario.objects.get(id=id)
    producto.delete()
    
    return redirect('inventario:home')

def editar(request, id):
    
    inventario=Inventario.objects.get(id=id) 
        
    fecha=inventario.ultima_compra
    #f=datetime.strftime(fecha, "%Y-%m-%d")
    print(fecha)
    
    if request.method=="POST":
        inventario.codigo=request.POST.get('codigo')
        inventario.detalle=request.POST.get('detalle')
        inventario.stock=request.POST.get('stock')
        inventario.stock_minimo=request.POST.get('stock_minimo')
        inventario.ultima_compra=request.POST.get('ultima_compra')
        inventario.observaciones=request.POST.get('observaciones')
       
        inventario.save()
        return redirect('inventario:home')

    context = {
        'inventario':inventario,
        'ultima_compra':datetime.datetime.strftime(fecha,"%Y-%m-%d")
    }
    return render(request, 'inventario/editar.html',context)  
    