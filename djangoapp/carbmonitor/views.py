from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

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

def calculadora(request):
    return render(request, "carbmonitor/calculadora.html")