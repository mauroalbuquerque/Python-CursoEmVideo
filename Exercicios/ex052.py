#Números Primos

num = int(input('Digite um número: '))

soma = 0

for c in range(num, 1, -1):
    if num % c == 0:
        soma += 1

if soma == 1:
    print('{} é um número primo!'.format(num))
else:
    print('{} não é um número primo!'.format(num))
