#Programa IBGE

resposta = 's'
maior = menor = num = cont = soma = 0

while resposta != 'n':
    num = int(input('Informe um número: '))

    soma += num

    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    cont += 1

    resposta = str(input('Vc deseja continuar [S/N]: ')).strip().lower()[0]

media = soma/cont

print(f'A média é de {media}')
print(f'O maior valor -> {maior}')
print(f'O menor valor -> {menor}')