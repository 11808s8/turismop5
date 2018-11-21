from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('roteiro/new/', views.roteiro_new, name='roteiro_new'),
    path('atrativo/new/', views.atrativo_new, name='atrativo_new'),
    path('ponto/new/', views.ponto_new, name='ponto_new')
]