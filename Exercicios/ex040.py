#Sistema de aprovação escolar

print('Sistema de aprovação escolar')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[41mReprovado!\033[m')
elif media >= 5 and media < 7:
    print('\033[43mRecuperação\033[m')
else:
    print('\033[42mAprovado!\033[m')