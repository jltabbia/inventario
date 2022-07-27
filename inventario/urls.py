from django.urls import path
from .views import InventarioHomeView, eliminar, InventarioCrearView

app_name='inventario'

urlpatterns = [
    path('', InventarioHomeView.as_view(), name='home'),
    path('crear/', InventarioCrearView.as_view(), name='crear'),
    path('eliminar/<int:id>', eliminar),

]
