from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, "carbmonitor/index.html")

def registro(request):
    form = UserCreationForm()
    return render(request, "carbmonitor/registro.html", {"form": form})

def calculadora(request):
    return render(request, "carbmonitor/calculadora.html")