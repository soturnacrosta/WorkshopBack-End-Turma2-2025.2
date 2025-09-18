from django.db import models

class Gatos(models.Model):
    # Armazena a URL da imagem.
    url = models.URLField(max_length=200)

    # Armazena se a imagem tem informações de raça (0 ou 1).
    has_breeds = models.IntegerField(default=0)
    
    # Armazena as IDs das categorias (ex: "1,4").
    category_ids = models.CharField(max_length=100, blank=True, null=True)
    
    # Armazena as IDs das raças (ex: "beng,siam").
    breed_ids = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.url