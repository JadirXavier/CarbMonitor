from django.urls import path
from carbmonitor.views import index

app_name = 'carbmonitor'

urlpatterns = [
    path('', index, name="index"),
]

