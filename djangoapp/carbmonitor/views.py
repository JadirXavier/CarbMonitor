from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "carbmonitor/index.html")

def calculadora(request):
    return render(request, "carbmonitor/calculadora.html")