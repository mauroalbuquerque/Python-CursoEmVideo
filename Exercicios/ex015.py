dias = int(input('Quantos dias você usou o carro: '))
km = float(input('Quantos Km vc rodou com o carro: '))

total = (dias * 60) + (km * 0.15)

print('Você rodou {} Km por {} dias com o carro.'.format(km, dias))
print('Total a pagar: R$ \033[032m{}\033[m'.format(total))