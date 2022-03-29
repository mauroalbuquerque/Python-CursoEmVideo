#Jogo de Impa/Par

from random import randint                                                      # Importando biblioteca para randomizar um número para a máquina

cont = 0                                                                        #Contador de vitórias

print('-' * 20)
print('{:^20')

while True:
    maquina = randint(0, 10)                                                    #Randomiza um número entre 0 ~ 10

    while True:                                                                 # Verifica se o jogador informou realmente um número
        jogador = input('Diga um valor: ')

        if jogador.isnumeric():
            jogador = int(jogador)
            break
        else:
            print('Valor informado não é um número. Tente Novamente!')

    while True:                                                                 # Verifica se o jogador selecionou uma opção válida, caso contrário solicita novamente
        escolha = input('Impar ou Par [I/P]: ').strip().lower()[0]

        if escolha == 'i' or escolha == 'p':
            break
        else:
            print('Opção Inválida! Tente Novamente...')

    resultado = maquina + jogador

    if escolha == 'p':
        if resultado % 2 == 0:
            print('Você venceu!')
            print('Vamos jogar novamente!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        if resultado % 2 == 1:
            print('Você Venceu!')
            print('Vamos jogar novamente')
            cont += 1
        else:
            print('Você perdeu!')
            break

print(f'Você venceu {cont}x')
print('Fim do programa!')