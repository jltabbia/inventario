from django.urls import path
from .views import crearView,eliminar,editar,InventarioHomeView

app_name='inventario'

urlpatterns = [
    path('', InventarioHomeView.as_view(), name='home'),
    path('crear/',crearView.as_view(),name='crear'),
    path('eliminar/<int:id>', eliminar),
    path('editar/<int:id>',editar)

]
