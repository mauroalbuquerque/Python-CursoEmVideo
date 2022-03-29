#Radar de Trânsito

velocidade = float(input('Digite a velocidade do veiculo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(velocidade, 'Multa: R$ {}'.format(multa))
else:
    print('Velocidade dentro do limite!')