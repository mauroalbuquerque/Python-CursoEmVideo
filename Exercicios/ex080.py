num = list()

for cont in range(0, 5):
    while True:
        valor = input('Informe um valor: ')

        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('Dados Inválidos. Tente Novamente!')

    if cont == 0 or valor > num[-1]:
        num.append(valor)
    else:
        for c in range(0, len(num)):
            if valor <= num[c]:
                num.insert(c, valor)
                break

    print(num)

print(num)