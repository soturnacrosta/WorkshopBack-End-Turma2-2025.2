from django import forms
from .models import Gatos

class GatosForm (forms.ModelForm):
    class Meta:
        model = Gatos 
        fields = ['url', 'has_breeds', 'category_ids', 'breed_ids', 'sub_id']