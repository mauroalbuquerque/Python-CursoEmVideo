#Função escreva com cabeçalho

def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

while True:
    texto = input('Informe o texto que vc deseja imprimir: ')

    escreva(texto)

    while True:
        resposta = input('Vc deseja informar mais outro texto [S/N]: ').strip().lower()[0]

        if resposta == 's' or resposta == 'n':
            break
        else:
            print('\033[41mInforme uma resposta válida!\033[m')

    if resposta == 'n':
        break

print('Fim do programa!')