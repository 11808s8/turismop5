from django import forms
from django.views.generic import UpdateView
from leaflet.forms.widgets import LeafletWidget
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password        
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Roteiro, Atrativo, Ponto, CustomUser, Pessoa_Fisica, Pessoa_Juridica

class RoteiroForm(forms.ModelForm):

    class Meta:
        model = Roteiro
        fields = ('nome', 'rota', 'guias', 'avaliacao',)


class AtrativoForm(forms.ModelForm):

    class Meta:
        model = Atrativo
        fields = ('nome', 'infos', 'ponto')

class PontoForm(forms.ModelForm):

    class Meta:
        model = Ponto
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}

class EditPonto(UpdateView):
    model = Ponto
    form_class = PontoForm
    template_name = 'ponto_new.html'

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('full_name', 'short_name', 'email','password')

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = Pessoa_Fisica
        fields = ('cpf', 'rg')

class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = Pessoa_Juridica
        fields = ('cnpj', 'razao_social', 'avaliacao','numero_registro')


class ClienteCadastroForm(CustomUserForm):
    cpf = forms.CharField(max_length=14)
    rg = forms.CharField(max_length=14)
    telefone = forms.IntegerField()

    class Meta(CustomUserForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_cliente = True

        hashed_password = make_password(self.cleaned_data.get('password'), None)
        user.password = hashed_password
        
        user.save()
        users_group = Group.objects.get(name='Clientes')
        user.groups.add(users_group)
        
        
        cpfLimpo = self.cleaned_data.get('cpf')
        print(self.cleaned_data.get('telefone'))
        telefoneLimpo = self.cleaned_data.get('telefone')
        rgLimpo = self.cleaned_data.get('rg')
        pessoa = Pessoa_Fisica.objects.create(usuario=user,cpf = cpfLimpo, telefone=telefoneLimpo,rg=rgLimpo)
        
        return user

class GuiaCadastroForm(CustomUserForm):
    razao_social = forms.CharField(max_length=150)
    cnpj = forms.CharField(max_length=14)
    telefone = forms.IntegerField()
    numero_registro = forms.IntegerField()
    class Meta(CustomUserForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guia = True

        hashed_password = make_password(self.cleaned_data.get('password'), None)
        user.password = hashed_password
        
        user.is_staff = True
        user.save()
        users_group = Group.objects.get(name='Guias')
        user.groups.add(users_group)
        cnpjLimpo = self.cleaned_data.get('cnpj')
        
        avaliacao = 0
        print(self.cleaned_data.get('telefone'))
        telefoneLimpo = self.cleaned_data.get('telefone')
        razao_socialLimpo = self.cleaned_data.get('razao_social')
        numeroRegistroLimpo = self.cleaned_data.get('numero_registro')
        pessoa = Pessoa_Juridica.objects.create(usuario=user,cnpj = cnpjLimpo, telefone=telefoneLimpo,razao_social=razao_socialLimpo,numero_registro=numeroRegistroLimpo,avaliacao=avaliacao)
        
        return user

