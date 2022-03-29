lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        resposta = (input('Deseja continuar [S/N]: ')).strip().lower()[0]
        if resposta in 'n':
            break
        else:
            if resposta in 's':
                continue
            else:
                print('')

print(lista)