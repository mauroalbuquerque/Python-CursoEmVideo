num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
cores = {'final': '\033[m'}
print('A soma entre \033[7;31m{}{} e \033[7:31m{}{} é igual a \033[42m{}{}'.format(num1, cores['final'], num2, cores['final'], soma, cores['final']))
