from django.urls import path
from djgeojson.views import GeoJSONLayerView
from catalogo_guias.models import Ponto
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('roteiro/new/', views.roteiro_new, name='roteiro_new'),
    path('atrativo/new/', views.atrativo_new, name='atrativo_new'),
    path('ponto/new/', views.ponto_new, name='ponto_new'),
    path('dados_todos_pontos', GeoJSONLayerView.as_view(model=Ponto), name='data')
]