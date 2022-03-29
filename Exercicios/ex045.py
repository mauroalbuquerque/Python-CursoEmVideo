#JOKENPO!!!

from random import randint
from time import sleep

item = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('JOKENPO!!')
print('Suas opções: ')
print('[ 1 ] - Pedra')
print('[ 2 ] - Papel')
print('[ 3 ] - Tesoura')

jogador = int(input('Qual vc escolhe: ')) - 1

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('==X==' * 5)
print('Você escolheu {}'.format(item[jogador]))
print('A máquina escolheu {}'.format(item[computador]))
print('==X==' * 5)

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Vc venceu!')
    elif jogador == 2:
        print('Máquina venceu!')
    else:
        print('\033[041mJogada Inválida!!\033[m')
        quit()
if computador == 1:
    if jogador == 0:
        print('Máquina venceu!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Vc venceu!')
    else:
        print('\033[041mJogada Inválida!!\033[m')
        quit()
if computador == 2:
    if jogador == 0:
        print('Vc venceu!')
    elif jogador == 1:
        print('Máquina venceu!')
    elif jogador == 2:
        print('Empate')
    else:
        print('\033[041mJogada Inválida!!\033[m')
        quit()
