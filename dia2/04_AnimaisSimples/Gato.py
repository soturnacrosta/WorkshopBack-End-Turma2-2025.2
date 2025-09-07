from Animal import Animal

class Gato (Animal):

    def __init__(self, corPelo, peso, altura): # precisa ter os parametros da classe mãe!!!

        super().__init__(corPelo, peso, altura)

    def falar (self):

        return "MIAU!!!"