from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Rubros

# Create your views here.
class GeneralHomeView(View):
    def get(self,request,*args,**kwargs):
        rubros=Rubros.objects.all()
        return render(request,'rubros/index.html',{'rubros':rubros})
   
class crearRubroView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'rubros/crear_rubro.html')   

    def post(self,request,*args,**kwargs):
        rubro=Rubros()
        rubro.detalle=request.POST.get('detalle')
        rubro.save()
        return redirect('rubros:home')
    
class crearSubRubroView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'rubros/crear_subrubro.html')   
