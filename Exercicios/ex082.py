#Lista de números Impares e Pares

lista = list()
par = list()
impar = list()

while True:
    while True:
        valor = input('Digite um valor: ')

        if valor.isnumeric():
            valor = int(valor)
            lista.append(valor)
            break
        else:
            print('Valor Inválido. Tente Novamente!')

    while True:
        resposta = input('Deseja continuar [S/N]: ').strip().lower()[0]

        if resposta != 's' and resposta != 'n':
            print('Valor Incorreto. Por favor, tente novamente!')
        else:
            break

    if resposta == 'n':
        break

print(lista)

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])

print(par)
print(impar)