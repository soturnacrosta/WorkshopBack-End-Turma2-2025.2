# def somar(a, b):
#    return a + b

# resultado = somar(10, "5")
# print(resultado)

# erro encontrado: TypeError
# ele está entrando a soma com o 5 como string!!
# versão corrigida:

def somar(a, b):
    
    try: 
        # tem que manter o codigo original!!
        return a + b

    except TypeError:
        
        try:
            #converte ambos para int
            return int(a) + int(b)

        except ValueError:
            #caso não conseguir, diz erro
            return "Erro: não foi possível converter os valores para números."

resultado = somar(10, "5") 

print(resultado)


