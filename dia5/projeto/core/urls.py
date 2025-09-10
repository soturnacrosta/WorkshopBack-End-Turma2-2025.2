from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), #aponta para def em views   
    path('consulta_cep/', views.Consulta_cep.as_view(), name='consulta_cep'),
    path('lista_ceps/', views.Lista_Cep.as_view(), name='lista_ceps'),               # lista todos os CEPs
    path('detalhes_cep/<int:pk>/', views.Details_Cep.as_view(), name='detalhes_cep'), # detalhes de um CEP específico
    path('deletar_cep/<int:pk>/', views.Delete_Cep.as_view(), name='deletar_cep'), 
]