from django.urls import path
from .views import CrearView, eliminar, editar, ProveedoresHomeView, ListaLocalidades

app_name='proveedores'

urlpatterns = [
    path('', ProveedoresHomeView.as_view(), name='home'),
    # path('crear/',crearView.as_view(),name='crear'),
    path('crear/',CrearView.as_view(),name='crear'),
    path('eliminar/<int:id>', eliminar),
    path('editar/<int:id>',editar),
    path('ListaLocalidades/<int:id>',ListaLocalidades),

]
