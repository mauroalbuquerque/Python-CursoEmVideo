#Calculadora

num = int(input('Digite um número de 1 a 9: '))

for c in range(0, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
