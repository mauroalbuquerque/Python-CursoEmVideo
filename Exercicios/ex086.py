#Matriz 3x3

matriz = [[], [], []]
soma_par = soma_col3 = maior_lin2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Informe o valor para a [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            soma_par += valor

        if coluna == 2:
            soma_col3 += valor

        if linha == 1 and coluna == 0:
            maior_lin2 = valor
        elif linha == 1 and (coluna == 1 or coluna == 2) and valor > maior_lin2:
            maior_lin2 = valor

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end='')

    print('')

print(f'A soma entre os números pares = {soma_par}')
print(f'A soma dos valores da 3 coluna = {soma_col3}')
print(f'O maior valor da 2 linha = {maior_lin2}')