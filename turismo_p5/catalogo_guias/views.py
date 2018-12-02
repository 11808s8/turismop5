from django import forms
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.core.serializers import serialize
from django.views.generic import CreateView
from django.contrib.auth import login

from .models import Roteiro, Atrativo, Ponto, CustomUser
from .forms import RoteiroForm, AtrativoForm, PontoForm, ClienteCadastroForm,GuiaCadastroForm



def index(request):
    return render(request, 'catalogo_guias/home.html')

def roteiro_new(request):
    if request.method == "POST":
        form = RoteiroForm(request.POST)
        if form.is_valid():
            Roteiro = form.save(commit=False)
            Roteiro.save()
            return redirect('/')
    else:
        form = RoteiroForm()
    return render(request, 'catalogo_guias/roteiro_new.html', {'form': form})

def atrativoGuiaAtrela(request):
    if(request.method == "POST"):
        dadosPost = request.POST # @TODO: CONTINUAR TRATANDO OS DADOS DAQUI
        print(request.user.id)
        # print(dadosPost)
        print(dadosPost["select"])
        # return redirect()
    todos_atrativos = Atrativo.objects.all()
    listaTodosAtrativos = list()
    for i in todos_atrativos:
        listaTodosAtrativos.append([ i.id , i.nome ])
    print(listaTodosAtrativos)
    return render(request, 'catalogo_guias/atrativo_guia.html', {'guiasatrativos':listaTodosAtrativos})

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

def dados_todos_pontos(request):
    points_geojson = serialize('geojson', Ponto.objects.all())
    return HttpResponse(points_geojson,content_type='application/json')

def dados_todos_atrativos(request):
    atrativos = Atrativo.objects.all()
    atrativos_json = serialize('json', atrativos)
    return HttpResponse(atrativos_json,content_type='application/json')

def dado_atrativo(request, id):
    atrativo = Atrativo.objects.get(id=id)
    return render(request, 'catalogo_guias/')

# class AtrativoDetailView(generic.DetailView):
#     model = Atrativo

def atrativo_detail_view(request, primary_key):
    try:
        atrativo = Atrativo.objects.get(pk=primary_key)
    except Atrativo.DoesNotExist:
        raise Http404('Atrativo não existe!')
    
    return render(request, 'catalogo_guias/atrativo_detail.html', context={'atrativo': atrativo})

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


class cliente_new(CreateView):
    model = CustomUser
    form_class = ClienteCadastroForm
    template_name = 'catalogo_guias/cadastroUsuario.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'cliente'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        customuser = form.save()
        login(self.request, customuser)
        return redirect('/')


class guia_new(CreateView):
    model = CustomUser
    form_class = GuiaCadastroForm
    template_name = 'catalogo_guias/cadastroUsuario.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'guia'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        customuser = form.save()
        login(self.request, customuser)
        return redirect('/')

