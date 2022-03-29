from random import randint
from time import sleep

num1 = randint(0, 5)

num2 = int(input('Digite um número entre 0 e 5: '))

print('PROCESSANDO...')
sleep(3)

if num1 == num2:
    print('Você acertou!', num1, num2)
else:
    if num2 > 5 or num2 < 0:
        print('Você digitou um valor fora da faixa!')
    else:
        print('Você errou!', num1, num2)
