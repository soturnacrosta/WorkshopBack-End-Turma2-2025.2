from django.db import models

# Create your models here.

class Pessoa (models.Model): ## todos os modelos herdam dessa classe

    nome = models.CharField(max_length=100) # varchar 
    idade = models.IntegerField() # int
    email = models.EmailField(unique=True) # define como unique

    def __str__(self): # define como será representado ao ser impresso!
        
        return self.nome