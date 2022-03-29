#Progressão Artimética usando o laço de repetição While

cont = 0

termo = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))

while cont < 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1