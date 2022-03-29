#Descubra a senha

soma = cont = 0

print('_' * 20)
print('{:^20}'.format('Descubra a Senha'))
print('_' * 20)

while True:
    senha = int(input('Senha: '))

    if senha == 999:
        break

    soma += senha
    cont += 1

print(f'Foram realizados {cont} tentativas')
print(f'A soma entre os valores informados é de {soma}')
