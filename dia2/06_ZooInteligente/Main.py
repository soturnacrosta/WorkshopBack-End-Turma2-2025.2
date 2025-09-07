from Animal import Animal 
from Gato import Gato
from Cachorro import Cachorro 
from Zoologico import Zoologico

animal1 = Animal("apollo", 2, "preto", 14, 1.72)
print(animal1.falar())
print(animal1.apresentar()) #incrementado!!

gato1 = Gato("happy", 3, "azul", 13, 20)
print(gato1.falar())

cachorro1 = Cachorro ("marley", 5, "branco colorido", 20, 1.56)
print(cachorro1.falar())

print ("################################")

zoo1 = Zoologico ()
zoo1.adicionar_animal(gato1)
zoo1.adicionar_animal(cachorro1)
zoo1.adicionar_animal(animal1)
zoo1.listar_animais()

print ("################################")

gato1 = zoo1.filtrar_por_tipo(Gato)
for gato in gato1:
    print(gato.falar())
