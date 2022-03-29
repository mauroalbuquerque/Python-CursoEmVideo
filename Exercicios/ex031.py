distancia = float(input('Digite a distancia da sua viagem: '))

if distancia > 200:
    print('Você pagará R$ 0,45 por cada Km. Total: {}'.format(distancia * 0.45))
else:
    print('Você irá pagar R$ 0,50 por cada Km. Total: {}'.format(distancia * 0.50))