#Calculadora com menu

escolha = 1
cont = 0

while 0 < escolha < 5:
    if cont == 0:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do programa')
    escolha = int(input(' Escolha um das opções: '))

    if escolha == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
        cont = 1
    elif escolha == 2:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
        cont = 1
    elif escolha == 3:
        if num1 > num2:
            print('{} > {}'.format(num1, num2))
        else:
            print('{} < {}'.format(num1, num2))
        cont = 1
    elif escolha == 4:
        cont = 0
