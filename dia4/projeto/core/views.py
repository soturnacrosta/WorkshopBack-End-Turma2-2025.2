from django.shortcuts import render
from .models import Endereco
from .forms import EnderecoForm
import requests

def home (request):
    return render(request, 'home.html') #apontado pelo views.home no urls
# Create your views here.
def consulta_cep(request):
    
    form = EnderecoForm(request.GET or None)
    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:

            data = response.json()
            print(data)

            endereco = Endereco (

                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                estado=data.get('uf')

            )

            endereco.save()
            return render(request, 'consulta_cep.html', {'endereco': endereco})
        
