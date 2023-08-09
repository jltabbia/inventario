from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import RubrosForm
from general.models import Rubros

# Create your views here.

class RubrosHomeView(View):
    def get(self,request,*args,**kwargs):
        rubros=Rubros.objects.all()
        
        return render(request,'rubros',{'rubros':rubros})
    

class crear(View):
    #if request.method == "GET":
    def get(self,request,*args,**kwargs):             
        form = RubrosForm()
        context = {
            'form':form
        }
        return render(request,'general/rubros.html',context=context)
    def post(self,request,*args,**kwargs):
        form = RubrosForm(request.POST)
        if form.is_valid():
            Rubros = form.save()
            form = RubrosForm()
        return redirect('/rubros/')
    