from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.conf import settings
from .models import Refeicao, Alimento
from .forms import RefeicaoForm
import requests
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    return render(request, "carbmonitor/index.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("carbmonitor:index")
    else:
        form = UserCreationForm()
    return render(request, "carbmonitor/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("carbmonitor:index")
    else:
        form = AuthenticationForm()
    return render(request, "carbmonitor/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("carbmonitor:index")
    else:
        return redirect("carbmonitor:index")

def buscar_alimento(request):
    if request.method == 'GET':
        query = request.GET.get('query', '').strip()

        if query:
            alimentos = Alimento.objects.filter(nome__icontains=query)[:10]
            

            alimentos_data = alimentos.values('nome', 'carboidratos_totais_100g', 'carboidratos_disponiveis_100g')

            return JsonResponse(list(alimentos_data), safe=False)

        return JsonResponse([], safe=False)

    return render(request, 'carbmonitor/calculadora.html') 
        
def calculadora(request):
    return render(request, "carbmonitor/calculadora.html")
