from rest_framework import viewsets
import requests
from .models import Endereco
from .serializers import EnderecoSerializer
class CEPViewsSet (viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def perform_create(self, serializer):
        cep = serializer.validated_data["cep"].replace("-", "") 
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            serializer.save(
                cep = cep,
                rua=data.get('logradouro', ''),
                bairro=data.get ('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', '')             

            )

        else :

            return super().perform_create(serializer)

            #serializer.save()


