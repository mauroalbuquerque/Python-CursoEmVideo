#Comparador de 3 números

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Check qual é o maior número
if num1 > num2 and num1 > num3:
    maior = num1
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3

#Check qual é o menor número
if num1 < num2 and num1 < num3:
    menor = num1
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

print(maior, menor)
