from django.urls import path
from . import views

app_name = 'carbmonitor'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('buscar_alimento/', views.buscar_alimento, name='buscar_alimento'),
]