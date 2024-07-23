from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, "carbmonitor/index.html")

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("carbmonitor:index")
    else:
        form = UserCreationForm()
    return render(request, "carbmonitor/registro.html", {"form": form})

def calculadora(request):
    return render(request, "carbmonitor/calculadora.html")