#Calculo IMC

print('Calculadora de IMC')

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

IMC = peso / (altura * altura)

print(IMC)

if IMC < 18.5:
    print('Você está abaixo do seu peso!')
elif IMC >= 18.5 and IMC < 25:
    print('Peso Ideal')
elif IMC >= 25 and IMC < 30:
    print('Sobrepeso')
elif IMC >= 30 and IMC < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')