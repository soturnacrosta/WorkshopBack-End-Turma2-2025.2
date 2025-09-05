import math

class FiguraGeometrica:

    def __init__ (self):

        pass

    @staticmethod
    def calcularCirculo (raio): # passe o raio através de circulo

        areaCirculo = math.pi * (raio ** 2)

        return {areaCirculo}

    @staticmethod
    def calcularTriangulo (base, altura):

        areaTriangulo = (base * altura) / 2

        return {areaTriangulo}

    @staticmethod
    def calcularTrianguloRetangulo (cateto1, cateto2):

        hipoTrianguloRetangulo = math.sqrt(cateto1**2 + cateto2**2) 

        return {hipoTrianguloRetangulo}

