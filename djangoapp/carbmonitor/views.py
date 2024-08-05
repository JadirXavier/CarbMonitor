from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.conf import settings
from .models import Refeicao
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
    print(settings.FOOD_API_KEY)
    if request.method == 'GET':
        query = request.GET.get('q')  # Obtém o nome do alimento da query string
        api_key = settings.FOOD_API_KEY  # Substitua pela sua chave de API no arquivo settings.py
        url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            alimentos = data.get('foods', [])
            for alimento in alimentos:
                print(alimento['description'])
            return JsonResponse({'alimentos': alimentos})
        else:
            return JsonResponse({'error': 'Erro na busca'})
    return render(request, 'carbmonitor/calculadora.html')  
        
def calculadora(request):
    return render(request, "carbmonitor/calculadora.html")
