from Animal import Animal

class Cachorro (Animal):

    def __init__ (self, nome, idade, corPelo, altura, peso): # precisa ter os parametros da classe mãe!!!

        super().__init__(nome, idade, corPelo, altura, peso)

    def falar (self):

        return "AU! AU!!!"
    

