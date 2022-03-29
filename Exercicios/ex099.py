mylist = list()

def maior(*lst):
    m = 0

    print(f'Os valores informados foram -> ', end=' ')
    for i, v in enumerate(lst[0]):
        print(v, end=' ')
        if i == 0:
            m = v
        else:
            if v > m:
                m = v

    print(f'\nO maior valor informado foi {m}')


while True:
    while True:
        qtd_num = input('Informe a quantidades de números que vc deseja inserir no sistema: ').strip().lower()

        if qtd_num.isnumeric():
            qtd_num = int(qtd_num)
            break
        else:
            print('\033[41mInforme um valor válido!\033[m')

    for c in range(0, qtd_num):
        while True:
            valor = input('Informe um número inteiro: ')

            if valor.isnumeric():
                mylist.append(int(valor))
                print('\033[42mValor salvo com sucesso!\033[m')
                break
            else:
                print('\033[41mInforme um valor válido!\033[m')

    maior(mylist)

    while True:
        resposta = input('Deseja fazer para mais valores [S/N]: ').strip().lower()[0]

        if resposta == 's' or resposta == 'n':
            break
        else:
            print('\033[41mInforme uma resposta válida!\033[m')

    if resposta == 'n':
        break

    mylist.clear()

print('Encerrando o programa!')
print('Programa encerrado!')
