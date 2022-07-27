from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from inventario import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('inventario',include('inventario.urls', namespace='invetario')),

]
