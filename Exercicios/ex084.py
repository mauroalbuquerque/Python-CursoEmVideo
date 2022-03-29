pessoas = list()
dados = list()
maiorPesoNome = list()
menorPesoNome = list()

maior_peso = menor_peso = cont = 0

while True:
    while True:
        nome = input('Nome: ')

        if nome.isalpha():
            dados.append(nome)
            break
        else:
            print('Informe um nome válido. Tente Novamente!')

    while True:
        peso = input('Peso: ')

        if peso.isnumeric():
            dados.append(peso)

            peso = int(peso)

            if cont == 0:
                maior_peso = menor_peso = int(peso)

                maiorPesoNome.append(nome)
                menorPesoNome.append(nome)

                cont += 1
            elif peso > maior_peso:
                maior_peso = peso
                maiorPesoNome.pop()
                maiorPesoNome.append(nome)

            elif peso < menor_peso:
                menor_peso = peso
                menorPesoNome.pop()
                menorPesoNome.append(nome)

            elif peso == maior_peso:
                maiorPesoNome.append(nome)
            elif peso == menor_peso:
                menorPesoNome.append(nome)

            break
        else:
            print('Informe um valor válido. Tente Novamente!')

    pessoas.append(dados[:])

    while True:
        resposta = input('Deseja continuar [S/N]: ').strip().lower()[0]

        if resposta != 's' and resposta != 'n':
            print('Informe uma resposta válida!')
        else:
            break

    dados.clear()

    if resposta in 'n':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas no sistema')
print(f'O maior peso cadastrado foi {maior_peso} Kg. Peso de {maiorPesoNome}')
print(f'O menor peso cadastrado foi {menor_peso} Kg. Peso de {menorPesoNome}')
