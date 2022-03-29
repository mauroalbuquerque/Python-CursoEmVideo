resposta = ''

while resposta != 'm' and resposta != 'f':
    resposta = str(input('Informe o seu sexo [M/F]: ').lower())

    if resposta != 'm' and resposta != 'f':
        print('Caracter Invalido!')

print(resposta)