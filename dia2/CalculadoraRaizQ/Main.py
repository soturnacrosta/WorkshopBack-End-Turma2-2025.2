import math

numero = float (input("Vamos calcular a raíz quadrada de um valor! Insira-o: "))

def calcularRaizQuadrada (numero): # não use self aqui!!!

    raizQuadrada = math.sqrt(numero)

    return f"A raiz quadrada de {numero} é: {raizQuadrada}"

print(calcularRaizQuadrada(numero)) # pode printar a função
    