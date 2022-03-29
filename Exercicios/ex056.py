#IBGE

nome_velho = ''
maior_idade = 0
cont_mulher = 0
soma_idade = 0.0

for c in range(0, 4):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    sexo = int(input('Informe o sexo (1 - Homem / 2 - Mulher): '))

    soma_idade += idade

    if idade > maior_idade and sexo == 1:
        nome_velho = nome
        maior_idade = idade

    if sexo == 2 and idade < 21:
        cont_mulher += 1

print('O homem mais velho é o {} com {} anos'.format(nome_velho, maior_idade))
print('{} mulheres tem menos de 21 anos'.format(cont_mulher))
print('A média de idade entre as pessoas informadas é de {} anos'.format(soma_idade/4))
