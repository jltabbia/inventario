from django.urls import path
from .views import CrearView, BuscarLoc, eliminar, editar, ClienteHomeView

app_name='clientes'

urlpatterns = [
    path('', ClienteHomeView.as_view(), name='home'),
    path('crear/',CrearView.as_view(),name='crear'),
    # path('crear/',crear,name='crear'),
    path('eliminar/<int:id>', eliminar),
    path('editar/<int:id>',editar),
    path('buscarloc',BuscarLoc),

]