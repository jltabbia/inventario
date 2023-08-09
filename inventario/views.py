
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required()

def HomeView(request):
       
    return render(request,'index.html',{})

def cerrarSesion(request):
    logout(request)
    return redirect('index')