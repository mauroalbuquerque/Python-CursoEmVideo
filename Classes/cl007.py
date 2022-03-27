# Ordem de precedência em operações matemáticas
# 1 > ()
# 2 > **
# 3 > * / // %
# 4 > + -

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

soma = num1 + num2
mult = num1 * num2
divisao = num1 / num2
divint = num1 // num2
expo = num1 ** num2

print('A soma é {},\no produto é {},\na divisão é {:.3f}'.format(soma, mult, divisao), end='')
print(', a divisao inteira é {} e a potência é {}'.format(divint, expo))
