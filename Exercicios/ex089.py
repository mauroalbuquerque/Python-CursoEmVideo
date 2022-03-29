#Programa Escola Antenor Reis

alunos = list()
notas = list()
controle = list()
media = float()

while True:
    while True:
        nome = input('Nome: ')

        if nome.isalpha():
            nome = str(nome)
            break
        else:
            print('Informe um nome válido!')

    controle.append(nome)

    for nota in range(1, 3):
        while True:
            valor = input(f'Nota {nota}: ')

            if valor.isnumeric():
                valor = int(valor)
                break
            else:
                print('Informe um número válido!')

        notas.append(valor)

    controle.append(notas[:])

    alunos.append(controle[:])
    controle.clear()
    notas.clear()

    while True:
        resposta = input('Deseja continuar [S/N]: ').strip().lower()[0]

        if resposta != 's' and resposta != 'n':
            print('Informe um valor válido: ')
        else:
            break

    if resposta == 'n':
        break

for cont in range(0, len(alunos)):
    media = (alunos[cont][1][0] + alunos[cont][1][1]) / 2
    print(f'{cont:<3} {alunos[cont][0]:.<10}{media:}')
