#Aula 21 - Funções

def parImpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Informe um número inteiro: '))

print(parImpar(num))
