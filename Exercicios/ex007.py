#Programa calcula a média de 2 notas de um aluno

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua outra nota: '))

media = (nota1 + nota2)/2

if media > 6:
    cor = '\033[32m'
if media == 6:
    cor = '\033[33m'
if media < 6:
    cor = '\033[31m'

print('A sua média é igual a {}{:.2f}'.format(cor, media))