# def validar_idade(idade):
#    if idade < 0 or idade > 120:
#        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
#    return f"Idade válida: {idade}"

# idade = int(input("Digite sua idade: "))
# print(validar_idade(idade))

# erro encontrado:
# SyntaxError, ValueError
# versão corrigida:

def validar_idade(idade): # o erro era aqui

    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

while True: # while apenas no try!

    try: 

        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
        break

    except SyntaxError: # o erro é na sintaxe do código!

        print ("Erro! Digite apenas números!!!")

    except ValueError:

        print ("Erro! Digite apenas números naturais!!!")