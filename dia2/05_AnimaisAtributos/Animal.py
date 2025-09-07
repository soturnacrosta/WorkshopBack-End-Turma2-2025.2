class Animal:

    def __init__ (self, nome, idade, corPelo, peso, altura):

        self.nome = nome
        self.idade = idade
        self.corPelo = corPelo
        self.peso = peso 
        self.altura = altura 

    def falar (self):
        
        return "Ele está falando..."
    
    def apresentar (self):

        return f"Ele se chama {self.nome} e tem {self.idade} anos de idade!" #incrementado!!

    