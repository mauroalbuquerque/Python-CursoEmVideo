#Programa 61 melhorado

cont = 10

termo = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))

while cont != 0:
    while cont > 0:
        print(termo, end=' ')

        termo += razao

        cont -= 1

    cont = int(input('\nVocê quer mostrar mais quantos termos: '))

print('Fim do programa')