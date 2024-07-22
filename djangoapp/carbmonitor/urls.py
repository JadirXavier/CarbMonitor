from django.urls import path
from . import views

app_name = 'carbmonitor'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('registro', views.registro, name='registro'),
]