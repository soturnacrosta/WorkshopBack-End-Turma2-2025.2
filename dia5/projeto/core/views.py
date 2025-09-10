from django.shortcuts import render
import requests
from django.views.generic import FormView
from .forms import EnderecoForm
from .models import Endereco

def home (request):
    return render(request, 'home.html') #apontado pelo views.home no urls
# Create your views here.
class Consulta_cep(FormView):
    template_name = "consulta_cep.html"
    form_class = EnderecoForm
    success_url = "/"  # Pode ser qualquer URL, não será usada aqui

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace("-", "").strip()
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "erro" not in data:
                endereco, created = Endereco.objects.update_or_create(
                    cep=cep,
                    defaults={
                        "rua": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "cidade": data.get("localidade", ""),
                        "estado": data.get("uf", "")
                    },
                )

                # Retorna a página com os dados do endereço
                return render(self.request, "resultado.html", {"endereco": endereco})

            else:
                form.add_error("cep", "CEP não encontrado na API.")
        else:
            form.add_error("cep", "Erro ao consultar a API do ViaCEP.")

        # Se caiu aqui, é porque deu erro
        return self.form_invalid(form)

    #class Viace




