#Exercicio 096

def area(larg, compr):
    print(f'Área = {larg} x {compr} = {larg * compr} [m²]')


while True:
    largura = input('Informe a largura do seu terreno: ')

    if largura.isnumeric():
        largura = int(largura)
        break
    else:
        print('\033[41mInforme um valor válido!\033[m')

while True:
    comprimento = input('Informe o comprimento do seu terreno: ')

    if comprimento.isnumeric():
        comprimento = int(comprimento)
        break
    else:
        print('\033[41mInforme um valor válido!\033[m')

area(largura, comprimento)
