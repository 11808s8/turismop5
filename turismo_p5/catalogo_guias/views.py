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
from django.db import connection

from .models import Roteiro, Atrativo, Ponto, CustomUser, Pessoa_Juridica
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
        print(dadosPost)
        dadosPost = dadosPost["select"]
        print(dadosPost)
        with connection.cursor() as cursor:
            insert = 'Insert into public.catalogo_guias_atrativo_guias (atrativo_id, pessoa_juridica_id) values ({},{})'.format(dadosPost, request.user.id)
            cursor.execute(insert)
        # print(dadosPost["select"])
        return redirect('index')
    q = ""
    with connection.cursor() as cursor:
        select = 'Select * from public.catalogo_guias_atrativo_guias where pessoa_juridica_id={};'.format(request.user.id)
        print(select)
        cursor.execute(select)
        q = cursor.fetchall()
    # print(q[0][1])
    listaAtrativos = list()
    for i in q:
        listaAtrativos.append(q[0][1])
    todos_atrativos = Atrativo.objects.exclude(id__in=listaAtrativos)
    listaTodosAtrativos = list()
    retorno = True
    if(len(todos_atrativos)==0):
        retorno = False
    else:
        for i in todos_atrativos:
            listaTodosAtrativos.append([ i.id , i.nome ])
    print(listaTodosAtrativos)
    return render(request, 'catalogo_guias/atrativo_guia.html', {'guiasatrativos':listaTodosAtrativos, 'possuiregistro':retorno})

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

def update_info_guia(request): 
    instance = get_object_or_404(CustomUser, id=request.user.id)
    pj = Pessoa_Juridica.objects.get(usuario_id=request.user.id)
    print(pj.razao_social)
    # form.razao_social = pj.razao_social
    # print(form.razao_social)
    
    if(request.POST):
        form = GuiaCadastroForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GuiaCadastroForm(request.POST or None, instance=instance, 
        initial={'razao_social':pj.razao_social, 'password':'', 'cnpj':pj.cnpj, 'telefone':pj.telefone, 'numero_registro':pj.numero_registro})
    return render(request, 'catalogo_guias/cadastroUsuario.html', {'form': form}) 


# class AtrativoDetailView(generic.DetailView):
#     model = Atrativo

def atrativo_detail_view(request, primary_key):
    try:
        atrativo = Atrativo.objects.get(pk=primary_key)
    except Atrativo.DoesNotExist:
        raise Http404('Atrativo não existe!')
    listaGuias = list()
    for a in atrativo.guias.all():
        pj = Pessoa_Juridica.objects.get(usuario_id = a.usuario_id)
        customuser = CustomUser.objects.get(id=a.usuario_id)
        listaGuias.append({'razao_social':pj.razao_social, 'cnpj':pj.cnpj,'telefone': pj.telefone,'email': customuser.email})
        # print(listaGuias)
    return render(request, 'catalogo_guias/atrativo_detail.html', context={'atrativo': atrativo, 'listaguias':listaGuias})

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

