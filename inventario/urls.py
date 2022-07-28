from django.urls import path
from .views import crear, eliminar, editar, InventarioHomeView

app_name='inventario'

urlpatterns = [
    path('', InventarioHomeView.as_view(), name='home'),
    # path('crear/',crearView.as_view(),name='crear'),
    path('crear/',crear,name='crear'),
    path('eliminar/<int:id>', eliminar),
    path('editar/<int:id>',editar)

]
