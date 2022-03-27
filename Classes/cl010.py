#Aula 10 - Condições

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2)/2

print(media)

print('Aprovado' if media >= 6 else 'Reprovado')

if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')