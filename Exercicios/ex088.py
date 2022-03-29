#Jogo da MegaSena

from random import randint
from time import sleep

jogos = list()
numeros = list()

qtd_jogos = int(input('Quantos jogos vc deseja fazer: '))

for cont in range(0, qtd_jogos):
    for num in range(0, 6):
        while True:
            valor = randint(1, 60)

            if not valor in numeros:
                numeros.append(valor)
                break

    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()

for imprimi in range(0, len(jogos)):
    print(f'Jogo {imprimi + 1} = {jogos[imprimi]}')
    sleep(1)
