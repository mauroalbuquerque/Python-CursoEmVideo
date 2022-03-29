aluno = dict()

while True:
    nome = input('Nome: ')

    if nome.isalpha():
        aluno['nome'] = str(nome)
        break
    else:
        print('Informe um nome válido!')

while True:
    media = input(f'A média de {aluno["nome"]}: ')

    if media.isnumeric():
        aluno['media'] = float(media)
        break
    else:
        print('Informe um número válido!')

if aluno['media'] >= 7:
    aluno['resultado'] = 'Aprovado'
else:
    aluno['resultado'] = 'Reprovado'

print(f'A média de {aluno["nome"]} é {aluno["media"]} e ele se encontra {aluno["resultado"]}')
