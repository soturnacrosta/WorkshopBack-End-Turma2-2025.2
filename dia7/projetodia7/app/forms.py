from django import forms
from .models import Gatos

class ConsultaGatosForm(forms.Form):

    breed_ids = forms.CharField(max_length=50, required=False, label="ID da Raça")
    category_ids = forms.CharField(max_length=50, required=False, label="ID da Categoria")


class GatosForm (forms.ModelForm):
    class Meta:
        model = Gatos
        fields = ['url', 'has_breeds', 'category_ids', 'breed_ids']