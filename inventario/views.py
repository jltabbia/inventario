from django.shortcuts import render
from django.views.generic import View
from .models import Inventario

# Create your views here.

class InventarioHomeView(View):
    def get(self, request,*args, **kwargs):
        inventario=Inventario.objects.all()
        print(inventario)
        context={
            inventario:inventario
        }
        return render(request, 'inventario/index.html', context)