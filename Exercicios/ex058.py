#Jogo da advinhação

from random import randint

maquina = randint(0, 10)

jogador = maquina + 1
cont = 0

while jogador != maquina:
    jogador = int(input('Digite um número entre 0 e 10: '))
    cont += 1

print(maquina, jogador, cont)
