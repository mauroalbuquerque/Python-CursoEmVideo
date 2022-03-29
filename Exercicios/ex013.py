#Calculadora salarial

salario = float(input('Informe o salário do funcionário: R$ '))

novosal = salario + salario*0.15

cores = {'final': '\033[m',
         'verde': '\033[032m',
         'vermelho': '\033[031m'}

print('O salário do funcionário acrescido de 15% passará de R$ {}{}{} para R$ {}{}{}'.format(cores['vermelho'], salario, cores['final'], cores['verde'], novosal, cores['final']))
