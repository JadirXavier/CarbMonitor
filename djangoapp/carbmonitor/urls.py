from django.urls import path
from . import views

app_name = 'carbmonitor'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
]