from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from inventario import urls
from clientes import urls
from proveedores import urls
from rubros import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('inventario/',include('inventario.urls', namespace='inventario')),
    path('clientes/',include('clientes.urls', namespace='clientes')),
    path('proveedores/',include('proveedores.urls', namespace='proveedores')),
    path('rubros/',include('rubros.urls', namespace='rubros')),

]
