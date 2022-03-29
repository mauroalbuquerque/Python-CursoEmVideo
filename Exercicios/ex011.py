#Calculadora de latas de tintas

largura = float(input('Qual a largura da sua parede: '))
altura = float(input('Qual a altura da sua parede: '))

area = largura * altura

qtdlatas = area / 2

print('A área da sua parede é de {}[m²].'.format(area))
print('Você irá precisar de {} litros de \033[43mtinta'.format(qtdlatas))
