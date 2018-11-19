from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Roteiro
from .forms import RoteiroForm
from django.shortcuts import redirect


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