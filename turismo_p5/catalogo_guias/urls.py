from django.urls import path, include
from djgeojson.views import GeoJSONLayerView
from catalogo_guias.models import Ponto
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    # path('roteiro/new/', views.roteiro_new, name='roteiro_new'),
    path('atrativo/new/', views.atrativo_new, name='atrativo_new'),
    path('ponto/new/', views.ponto_new, name='ponto_new'),
    path('dados_todos_pontos', GeoJSONLayerView.as_view(model=Ponto), name='data'),
    path('contas/cadastro/usuario/cliente', views.cliente_new.as_view(), name='cadastro_cliente'),
    path('contas/cadastro/usuario/guia', views.guia_new.as_view(), name='cadastro_guia'),
    path('dados_todos_atrativos',views.dados_todos_atrativos, name='dados_atrativos'),
    path('atrativo/<int:primary_key>', views.atrativo_detail_view, name='atrativo_detail'),
    path('atrativos/guia', views.atrativoGuiaAtrela, name='atrativo_guia_atrela'),
    path('accounts/', include('django.contrib.auth.urls')),
]