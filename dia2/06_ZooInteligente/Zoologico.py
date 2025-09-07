from Animal import Animal 

class Zoologico ():

    def __init__ (self): #sempre ter self!!

        self.animais_lista = [] #declara lista vazia

    def adicionar_animal (self, animal):

        self.animais_lista.append(animal) 
        print ("Animal adicionado com sucesso!") #degug! não me mate!

    def listar_animais (self):

        for animal in self.animais_lista:
           
            print(animal.apresentar()) #apresentando!!!
            print(animal.falar()) #falando!
            ##ele se apresenta e depois fala

    def filtrar_por_tipo (self, tipo_animal):

        animais_filtrados = [] #filtrando com isinstance!!

        for animal in self.animais_lista:

            if isinstance (animal, tipo_animal): #verifica o tipo de cada animal!

                animais_filtrados.append(animal)

        return animais_filtrados