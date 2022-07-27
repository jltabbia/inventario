import re
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Inventario

# Create your views here.

class InventarioHomeView(View):
    def get(self, request,*args, **kwargs):
        inventario=Inventario.objects.all()
        return render(request, 'inventario/index.html', {"inventario":inventario})
    
class InventarioCrearView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'inventario/crear.html',{})
    
    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            producto=Inventario.new()
            producto.codigo=request.get('codigo')
            producto.save()
            
            return redirect('inventario:home')        
        
def eliminar(request, id):
    producto=Inventario.objects.get(id=id)
    producto.delete()
    
    return redirect('inventario:home')
    