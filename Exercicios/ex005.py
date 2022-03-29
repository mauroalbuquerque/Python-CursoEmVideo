num1 = int(input('Digite um número inteiro: '))

cores = {'final': '\033[m'}

print('O seu sucessor é \033[42m{}{} e seu antecessor é \033[41m{}{}'.format(num1 + 1, cores['final'], num1 - 1, cores['final']))