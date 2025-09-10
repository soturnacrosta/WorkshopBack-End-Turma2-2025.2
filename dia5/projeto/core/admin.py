from django.contrib import admin
from .models import Endereco
# Register your models here.

class EnderecoAdmin(admin.ModelAdmin):
    search_fields = ['cep']
admin.site.register(Endereco, EnderecoAdmin)