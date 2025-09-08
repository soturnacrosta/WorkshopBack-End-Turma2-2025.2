# dados = {
#    "nome": "Isaac ",
#    "idade": 25,
#    "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")

# print(f"O valor da chave '{chave}' é: {dados[chave]}")

# erros encontrados: KeyError
# o erro se dá ao não digitar as chaves registradas!
# versão corrigida:

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

try: 

    #o print é que lança os erros!
    print(f"O valor da chave '{chave}' é: {dados[chave]}")

except KeyError:

    valor = dados.get(chave, "Chave não encontrada!")
    print (f"Chave '{chave}': {valor}")
    
