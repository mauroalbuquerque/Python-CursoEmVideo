#Alistamento militar

from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))

idade = date.today().year - ano

if idade < 18 and idade > 0:
    print('\033[43mAlistamento chegando. Faltam {} anos\033[m'.format(18 - idade))
elif idade > 18:
    print('\033[41mAlistamento vencido em {} anos.\033[m'.format(idade - 18))
else:
    print('\033[42mVocê está no tempo para o alistamento. Por favor, compareça ao quartel mais próximo.\033[m')

print(idade)