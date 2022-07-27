from django.urls import path
from .views import InventarioHomeView

app_name='inventario'

urlpatterns = [
    path('', InventarioHomeView.as_view(), name='home'),

]
