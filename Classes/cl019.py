#Aula 19 - Mundo 3 - Dicionários

dados = dict()

dados = {'nome': 'Pedro','idade': 25}
dados['sexo'] = 'm'

print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])

del dados['idade']

print(dados)

filme = {
    'titulo': 'Star Wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Mauro', 'sexo':'m', 'idade': 24}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(k, v)

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 91.5

print(pessoas)

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))

    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
