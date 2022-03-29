from random import randint

numeros = list()

def sorteia():
    for cont in range(0, 5):
        numeros.append(randint(0, 9))

def somaPar(*num):

    soma = 0

    print('Os valores informados foram -> ', end=' ')
    for valores in num[0]:
        print(valores, end=' ')
        if valores % 2 == 0:
            soma += valores
    print()
    print(f'A soma dos números pares sorteados é igual a {soma}')

sorteia()
somaPar(numeros)
