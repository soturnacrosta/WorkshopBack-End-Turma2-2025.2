from django.shortcuts import render
import requests
from django.views.generic import FormView, DetailView, ListView, DeleteView
from .forms import EnderecoForm
from .models import Endereco
from django.urls import reverse_lazy #posições relativas!

# ... outros imports
def home (request):
    return render(request, 'home.html') #apontado pelo views.home no urls
# Create your views here.
class Consulta_cep (FormView):
    template_name = "viacep/consulta_cep.html"
    form_class = EnderecoForm
    success_url = reverse_lazy ('consulta_cep') #cuidado com o template

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace("-", "")
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "erro" not in data:

                cep_obj, created = Endereco.objects.get_or_create(
                    cep=cep,
                    defaults={

                       "rua": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "cidade": data.get("localidade", ""),
                        "estado": data.get("uf", "")
                    },
                )

                contexto = { ################################################################################################

                    'form': form,
                    'endereco': cep_obj,  # 'endereco' é o nome da variável que o template vai usar

                }
                                                                        ########################################################
                return render(self.request, self.template_name, contexto) #AQUI QUE FAZ OS DADOS APARECEREM NO RENEDER!!!!!!!!!!!
                                                                        ########################################################

            else: 

                form.add_error("cep", "CEP não encontrado na API em Endereco.")
                return self.form_invalid(form)
            
        else:

            form.add_error("cep", "Erro ao consultar CEP na API em Endereco.")
            return self.form_invalid(form)
        
        #form.save() o save duplicaria os objetos retornados!! 
        return super().form_valid(form)


    #class Viace
class Lista_Cep (ListView):
    model = Endereco 
    template_name = "viacep/viacep_list.html"
    context_object_name = "ceps"

class Details_Cep (DetailView):
    model = Endereco
    template_name = "viacep/viacep_detail.html"
    context_object_name = "ceps"

class Delete_Cep (DeleteView):
    model = Endereco
    template_name = "viacep/viacep_delete.html"
    context_object_name = "ceps"
    




