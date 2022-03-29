#Analisador de triângulos

lado1 = float(input('Informe o lado A: '))
lado2 = float(input('Informe o lado B: '))
lado3 = float(input('Informe o lado C: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('É possivel formar um triângulo!')
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno!')
else:
    print('Não é possivel formar um triângulo com os valores informados!')
