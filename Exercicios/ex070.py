total = totmil = cont = 0

while True:
    produto = str(input('Nome do produto: ')).strip().lower()
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    if preco > 1000:
        totmil += 1

    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]

    if resposta == 'n':
        break

print('{:-^40}'.format('Fim do Programa'))
print(f'\nO total da compra foi R$ {total}')
print(f'{totmil} custaram mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
