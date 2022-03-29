lista = [[], []]

for c in range(1, 8):
    while True:
        valor = input(f'Digite o {c}º valor: ')

        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('Informe um valor válido!')

    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()

print(f'Os números pares informados foram: {lista[0]}')
print(f'Os números impares informados foram: {lista[1]}')
