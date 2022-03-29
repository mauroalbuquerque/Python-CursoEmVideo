num = list()

while True:
    while True:
        valor = input('Digite um valor: ')

        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('Valor Incorreto. Por favor, tente novamente!')

    num.append(valor)

    while True:
        resposta = input('Deseja continuar [S/N]: ').strip().lower()[0]

        if resposta != 's' and resposta != 'n':
            print('Dados Incorretos. Por favor, tente novamente!')
        else:
            break

    if resposta == 'n':
        break

print(num)

print(f'Foram inseridos {len(num)}')

num.sort(reverse=True)

print(f'A lista em ordem decrescente -> {num}')

if 5 in num:
    print('O valor 5 se encontra na lista')
else:
    print('O valor 5 não se encontra na lista')