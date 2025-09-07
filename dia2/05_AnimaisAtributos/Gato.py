from Animal import Animal

class Gato (Animal):

    def __init__(self, nome, idade, corPelo, peso, altura): # precisa ter os parametros da classe mãe!!!

        super().__init__(nome, idade, corPelo, peso, altura)

    def falar (self):

        return "MIAU!!!"