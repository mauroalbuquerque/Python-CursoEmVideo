#Programa de formas de pagamento

preço = float(input('Informe o preço do seu produto: R$ '))

print('1 - Dinheiro + 10% de desconto')
print('2 - À vista no cartão + 5% de desconto')
print('3 - 2x no cartão')
print('4 - 3x ou mais + 20% de juros')
seleção = int(input('Selecione a forma de pagamento: '))

preçoold = preço

if seleção == 1:
    preço = preço - preço * 0.1
elif seleção == 2:
    preço = preço - preço * 0.05
elif seleção == 3:
    preço = preço
elif seleção == 4:
    preço = preço * 1.2
else:
    print("\033[41mForma de pagamento inválida!\033[m")
    quit()

print('O valor do prooduto era de R$ {} agora é de R$ {}'.format(preçoold, preço))
