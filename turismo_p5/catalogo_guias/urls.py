from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('roteiro/new/', views.roteiro_new, name='roteiro_new'),
]