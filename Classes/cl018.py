teste = list()
pessoas = list()

teste.append('Mauro')
teste.append(24)

pessoas.append(teste[:])

teste[0] = 'Maria'
teste[1] = 30

pessoas.append(teste[:])

print(pessoas)

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoas = list()
dados = list()

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))

    pessoas.append(dados[:])

    dados.clear()

for p in pessoas:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} não é maior de idade')
