#Programa Nacional de Natação

from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 20:
    print('Sênior')
else:
    print('Master')

print(idade)
