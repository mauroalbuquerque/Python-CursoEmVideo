#Calculadora da hipotenusa

from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é {}{:.5f}{}'.format('\033[42m',hypot(oposto, adjacente), '\033[m'))
