# numeros = [10, 20, 30]
# indice = int(input("Digite um índice para acessar a lista: ")) 

# print(numeros[indice])

# erro encontrado: IndexError
# código corrigido:

numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

try:

    print(numeros[indice])

except IndexError:

    print (f"Índice não encontrado!!! Digite um índice entre {len(numeros)} e 0")

except ValueError:

    print("Por favor, digite um número válido!!!")  