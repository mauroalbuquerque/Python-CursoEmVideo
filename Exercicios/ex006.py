print('=X=' * 10)
num1 = float(input('Digite um número: '))

dobro = num1 * 2
triplo = num1 * 3
raiz = num1 ** (1/2)

cores = {'final': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m'}

print('O {}dobro{} de {} = {}'.format(cores['verde'], cores['final'], num1, dobro))
print('O {}triplo{} de {} = {}'.format(cores['amarelo'], cores['final'], num1, triplo))
print('A {}raiz{} de {} = {:.2f}'.format(cores['vermelho'], cores['final'],num1, raiz))