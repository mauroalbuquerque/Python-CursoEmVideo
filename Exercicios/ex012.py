#Calculadora de desconto

preço = float(input('Informe o preço do produto: R$ '))

desconto = preço - preço * 0.05

print('O valor do produto com \033[43mdesconto\033[m é R$ {}'.format(desconto))
