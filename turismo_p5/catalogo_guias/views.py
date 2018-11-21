from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Roteiro, Destino, Ponto
from .forms import RoteiroForm, AtrativoForm, PontoForm



def index(request):
    return render(request, 'catalogo_guias/home.html')

def roteiro_new(request):
    if request.method == "POST":
        form = RoteiroForm(request.POST)
        if form.is_valid():
            Roteiro = form.save(commit=False)
            Roteiro.save()
            return redirect('home.html')
    else:
        form = RoteiroForm()
    return render(request, 'catalogo_guias/roteiro_new.html', {'form': form})

def atrativo_new(request):
    if request.method == "POST":
        form = AtrativoForm(request.POST)
        if form.is_valid():
            Atrativo = form.save(commit=False)
            Atrativo.save()
            return redirect('/')
    else:
        form = AtrativoForm()
    return render(request, 'catalogo_guias/atrativo_new.html', {'form': form})

def ponto_new(request):
    if request.method == "POST":
        form = PontoForm(request.POST)
        if form.is_valid():
            Ponto = form.save(commit=False)
            Ponto.save()
            return redirect('catalogo_guias/roteiro_new.html')
    else:
        form = PontoForm()
    return render(request, 'catalogo_guias/ponto_new.html', {'form': form})
