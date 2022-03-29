nome = input('Digite o seu nome: ')

print(nome.upper())
print(nome.lower())

nome = nome.split()

primeironome = nome[0]

nome = ''.join(nome)

print('Seu nome tem {} letras'.format(len(nome)))

print('O seu primeiro nome ({}) tem {} letras'.format(primeironome, len(primeironome)))