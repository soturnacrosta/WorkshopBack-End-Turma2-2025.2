from django.shortcuts import render, redirect
from .models import Gatos
from .forms import GatosForm
import requests
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy

def home (requests):

    return render (requests, 'home.html')

class ConsultaGato(View):
    def get(self, request):
        # Exemplo: buscar 3 imagens de gatos da raça Bengal (beng) com chapéu (categoria 1)
        url = "https://api.thecatapi.com/v1/images/search?limit=3&breed_ids=beng&category_ids=1"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            dados = response.json()
            for item in dados:
                category_ids = "1"        # já sabemos que filtramos pela categoria 1
                breed_ids = "beng"        # raça Bengal
                url_imagem = item.get('url')

                Gatos.objects.create(
                    url=url_imagem,
                    has_breeds=item.get('has_breeds', 0),
                    category_ids=category_ids,
                    breed_ids=breed_ids
                )

        return redirect('consulta_gato.html')
    
class GatoCreateView (CreateView):
     
    model = Gatos 
    form_class = GatosForm
    template_name = "gatos_create.html"
    success_url = reverse_lazy('gatos_detail')

class GatosListView (ListView):
     
    model = Gatos 
    template_name = "gatos_list.html"
    context_object_name = "gatos"

class GatoDetailView (DetailView):
     
    model = Gatos 
    template_name = "gatos_detail.html"
    context_object_name = "gatos"

class GatoUpdateView(UpdateView):
    model = Gatos
    form_class = GatosForm
    template_name = 'gato_form.html'
    success_url = reverse_lazy('listar_gatos')

class GatoDeleteView(DeleteView):
    model = Gatos
    template_name = 'gato_confirm_delete.html'
    success_url = reverse_lazy('listar_gatos')