#Comparar entre 2 números

print('Comparador entre 2 números')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('{} > {}'.format(num1, num2))
elif num2 > num1:
    print('{} < {}'.format(num1, num2))
else:
    print('{} = {}'.format(num1, num2))
