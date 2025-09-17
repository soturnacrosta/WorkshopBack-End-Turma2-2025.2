from django.urls import path
from .views import (home, ConsultaGato, GatosListView, GatoDetailView, GatoCreateView, GatoUpdateView, GatoDeleteView
)

urlpatterns = [

    path('', home, name='home'),
    path('consulta/', ConsultaGato.as_view(), name='consulta_gato'),
    path('gatos/', GatosListView.as_view(), name='listar_gatos'),
    path('gatos/<int:pk>/', GatoDetailView.as_view(), name='detalhar_gato'),
    path('gatos/novo/', GatoCreateView.as_view(), name='criar_gato'),
    path('gatos/<int:pk>/editar/', GatoUpdateView.as_view(), name='editar_gato'),
    path('gatos/<int:pk>/excluir/', GatoDeleteView.as_view(), name='excluir_gato'),
    
]
