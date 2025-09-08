from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home') # quando tá vazio é a primeira aba!!!
]
