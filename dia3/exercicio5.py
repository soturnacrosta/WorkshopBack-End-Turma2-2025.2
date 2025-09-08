# def dividir(a, b):
#    return a / b

# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")

# resultado = dividir(int(num1), int(num2))
# print(f"Resultado: {resultado}")

# erro encontrado:
# ValueError, ZeroDivisionError
# versão corrigida:

def dividir(a, b):
    return a / b

try:

    num1 = int (input("Digite o primeiro número: ")) #inserir a conversão logo no input!
    num2 = int (input("Digite o segundo número: "))

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")

except ValueError:

    print ("Erro! Digite apenas números!")

except ZeroDivisionError:

    print ("Erro! Não pode ser dividido por zero!")