from random import randint

jogadores = dict()
ranking = list()

for cont in range(1, 6):
    jogadores[f'Jogador{cont}'] = randint(1, 6)

print(jogadores)
