from django import forms
from django.views.generic import UpdateView
from leaflet.forms.widgets import LeafletWidget

from .models import Roteiro, Atrativo, Ponto

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