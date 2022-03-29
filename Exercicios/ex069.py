#Programa IBGE

idade_maior = qtd_homem = mulher_menor = 0

while True:
    while True:
        idade = input('Idade: ')

        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print('Favor, informa um valor válido! Tente novamente!')

    while True:
        sexo = input('Sexo: ').strip().lower()[0]

        if sexo != 'm' and sexo != 'f':
            print('Opção Inválida! Entre com uma opção válida!')
        else:
            break


    while True:
        resposta = input('Deseja continuar [S/N]: ').strip().lower()[0]

        if resposta != 's' and resposta != 'n':
            print('Opção Inválida! Tente Novamente...')
        else:
            break

    if idade > 18:
        idade_maior += 1

    if sexo == 'm':
        qtd_homem += 1

    if sexo == 'f' and idade < 20:
        mulher_menor += 1

    if resposta == 'n':
        break

print(f'{idade_maior} tem mais de 18 anos')
print(f'Foram cadastrados {qtd_homem} homens')
print(f'{mulher_menor} mulheres tem menos de 20 anos de idade')

print('Fim do programa!')