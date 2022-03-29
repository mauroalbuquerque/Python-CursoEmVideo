soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        soma += c
        cont += 1

print('\n', soma, cont)
