#Conversor de moeda

valor = float(input('Digite um valor em reais: R$ '))

valordol = valor / 3.27

print('Você tem em \033[33mdólar\033[m US$ {:.2f}'.format(valordol))
