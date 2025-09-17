from django.db import models

# Create your models here.
class Gatos (models.Model):

    sub_id = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)
    has_breeds = models.BooleanField(default=False) # Booleano para indicar se a imagem tem informações de raça
    category_ids = models.JSONField(default=list)
    breed_ids = models.JSONField(default=list)  # Usando JSONField para armazenar IDs de raças como uma lista

def __str__(self):
        return self.url
