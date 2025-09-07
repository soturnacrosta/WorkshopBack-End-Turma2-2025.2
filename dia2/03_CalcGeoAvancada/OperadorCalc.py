from FiguraGeometrica import FiguraGeometrica

class Operador:

    def __init__ (self):

        pass 

    def usarCalculoCirculo (self):

        raio = float (input ("Vamos calcular a área do círculo. Digite o raio em números: "))
        
        area = FiguraGeometrica.calcularCirculo(raio) #tem que chamar o metodo antes de dar return

        print (f"A área do círculo é: {area}") # pode printar para retornar
    
    def usarCalcTriangulo (self):

        base = float (input ("Vamos calcular a área do triângulo! Digite a base em números: "))
        altura = float (input ("Agora digite a altura: "))

        area = FiguraGeometrica.calcularTriangulo(base, altura)

        print (f"A área do triângulo é {area}")
    
    def usarCalcTriangRet (self): #não precisa passar os parametros de instancia, você vai pedir no input. iria sobrescrever
        
        cat1 = float (input ("Vamos calcular a hipotenusa do triângulo retângulo! Digite o primeiro catêto em números: "))
        cat2 = float (input ("Agora digite ")) 
        
        hipotenusa = FiguraGeometrica.calcularTrianguloRetangulo(cat1, cat2)

        print (f"A hipotenusa é: {hipotenusa}")