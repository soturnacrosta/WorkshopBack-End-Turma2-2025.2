import math 

numero = float (input("Vamos arredondar um valor! Digite o valor: "))

def arredondarCima (numero):

    arredondarTeto = math.ceil(numero)
    
    return arredondarTeto

def arredondarBaixo (numero):

    arredondarPiso = math.floor(numero)

    return arredondarPiso

def arredondarProximo (numero):

    arredondarProx = round(numero) # é uma função e não parte da classe math

    return arredondarProx

print (arredondarCima(numero))
print (arredondarBaixo(numero))
print (arredondarProximo(numero))
    

