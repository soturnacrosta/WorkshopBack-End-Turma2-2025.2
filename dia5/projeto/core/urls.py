from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), #aponta para def em views   
    path('consulta_cep/', views.Consulta_cep.as_view(), name='consulta_cep')
]