from Animal import Animal

class Cachorro (Animal):

    def __init__ (self, corPelo, altura, peso): # precisa ter os parametros da classe mãe!!!

        super().__init__(corPelo, peso, altura)

    def falar (self):

        return "AU! AU!!!"
    

