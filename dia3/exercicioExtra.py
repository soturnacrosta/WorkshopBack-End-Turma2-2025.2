"""
def calcular_media(notas):
soma = sum(notas)
quantidade = len(notas)
return soma / quantidade

notas = [8, 9, "10", 7]
media = calcular_media(notas)
print(f"Média: {media:.2f}")
"""

# erro encontrado:
# TypeError, ValueError
# versão corrigida:

def calcular_media(notas):
    soma = sum(notas)
    nota = soma / len(notas)
    return nota

try:

    nota1 = float (input ("Vamos calcular a média de suas notas! Digite a primeira nota: "))
    nota2 = float (input ("Agora digite sua segunda nota: "))
    nota3 = float (input ("Digite sua terceira nota: "))
    nota4 = float (input ("Por fim, sua quarta nota: "))

    if (nota1 >= 0 and nota1 <= 10 and
        nota2 >= 0 and nota2 <= 10 and
        nota3 >= 0 and nota3 <= 10 and
        nota4 >= 0 and nota4 <= 10):

        notas = [nota1, nota2, nota3, nota4]
        media = calcular_media(notas)
        print(f"Média: {media:.2f}")
 
    else:

        print("Erro! Digite valores entre 0 e 10!")

except TypeError:

    print ("Erro! Digite apenas números no código!!!")

except ValueError:

    print ("Erro! Digite apenas números!!!")
