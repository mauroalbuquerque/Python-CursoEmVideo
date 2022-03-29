lista = list()
lista_maior = list()

maior = menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite o {c + 1}ª valor: ')))
    if c == 0:
        maior = menor = lista[0]
        lista_maior = c
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('A sua lista possui os seguintes valores:', lista)

print(f'O maior valor digitado foi {maior} e ele apareceu nas seguintes posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end=' ')

print(f'\nO menor valor digitado foi {menor} e ele apareceu nas seguintes posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(i, end=' ')
