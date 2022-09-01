from django.urls import path
from .views import GeneralHomeView, crearRubroView, crearSubRubroView

app_name='rubros'

urlpatterns = [
    path('', GeneralHomeView.as_view(), name='home'),
    path('crearRubro',crearRubroView.as_view(),name='rubro'),
    path('crearSubRubro',crearSubRubroView.as_view(),name="subrubro"),
]