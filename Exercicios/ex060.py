#Calculando Fatorial

fatorial = 1

num = int(input('Informe um número: '))

controle = num

while controle > 0:
    print(f'{controle}', end='')
    print(' x ' if controle > 1 else ' = ', end='')
    fatorial *= controle
    controle -= 1

print(fatorial)
