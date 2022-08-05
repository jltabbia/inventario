from django.urls import path
from .views import crear, eliminar, editar, ClienteHomeView, buscarLoc

app_name='clientes'

urlpatterns = [
    path('', ClienteHomeView.as_view(), name='home'),
    # path('crear/',crearView.as_view(),name='crear'),
    path('crear/',crear,name='crear'),
    path('eliminar/<int:id>', eliminar),
    path('editar/<int:id>',editar),
    path('buscarloc/<int:id>',buscarLoc),

]