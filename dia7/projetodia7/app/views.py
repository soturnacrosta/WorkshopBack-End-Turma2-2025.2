from django.shortcuts import render, redirect
from .models import Gatos
from .forms import GatosForm, ConsultaGatosForm
import requests
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy

def home (requests):

    return render (requests, 'home.html')


class ConsultaGato(View):
    # Este método exibe o formulário quando a página é acessada pela primeira vez.
    def get(self, request):
        form = ConsultaGatosForm()
        return render(request, 'consulta_gato.html', {'form': form})

    # Este método processa os dados do formulário quando ele é submetido.
    def post(self, request):
        form = ConsultaGatosForm(request.POST)

        if form.is_valid():
            breed_ids = form.cleaned_data.get('breed_ids', '')
            category_ids = form.cleaned_data.get('category_ids', '')
            
            url = f"https://api.thecatapi.com/v1/images/search?limit=3"
            
            if breed_ids:
                url += f"&breed_ids={breed_ids}"
            if category_ids:
                url += f"&category_ids={category_ids}"
            
            response = requests.get(url, verify=False)
            
            if response.status_code == 200:
                dados = response.json()
                
                if dados:
                    item = dados[0]
                    novo_gato = Gatos.objects.create(
                        url=item.get('url'),
                        has_breeds=item.get('has_breeds', 0),
                        category_ids=category_ids,
                        breed_ids=breed_ids
                    )
                    return redirect('detalhar_gato', pk=novo_gato.pk)
                else:
                    context = {'form': form, 'mensagem': 'Nenhum gato encontrado para este filtro.'}
                    return render(request, 'consulta_gato.html', context)
            else:
                context = {'form': form, 'mensagem': f'Erro ao consultar a API. Status: {response.status_code}'}
                return render(request, 'consulta_gato.html', context)
        
        return render(request, 'consulta_gato.html', {'form': form})
        
class GatoCreateView (CreateView):
    model = Gatos 
    form_class = GatosForm
    template_name = "gatos_create.html"

    def get_success_url(self):
        return reverse_lazy('detalhar_gato', kwargs={'pk': self.object.pk})

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