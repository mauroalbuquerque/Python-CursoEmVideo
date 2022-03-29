#Forma triangulo

num1 = float(input('Digite o valor do lado a: ').strip())
num2 = float(input('Digite o valor do lado b: ').strip())
num3 = float(input('Digite o valor do lado c: ').strip())

if num2 - num3 < num1 < num2 + num3 and num1 - num3 < num2 < num1 + num3 and num2 - num1 < num3 < num2 + num1:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
