#Programa Tabuada
#Este programa tem com finalidade a exibição da tabuada de varios valores
#o programa será encerrado quando o valor infomado pelo usuário for negativo

print('-' * 20)
print('{:^20}'.format('Programa Tabuada'))
print('-' * 20)

while True:
    while True:
        num = input('Quer ver a tabuada de qual valor: ')

        if num.isnumeric() or int(num) < 0:
            num = int(num)
            break
        else:
            print('Não é um número! Tente Novamente!')
            print('-' * 20)

    c = 0

    if num < 0:
        break

    print('-' * 20)

    while True:
        print(f'{num} x {c} = {num * c}')

        if c == 10:
            break

        c += 1

    print('-' * 20)

print('Programa Tabuada encerrado com sucesso!')