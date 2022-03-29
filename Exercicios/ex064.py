#Programa de senha

cont = soma = entrada = 0

while entrada != 999:
    entrada = int(input('Entre com a senha: '))
    
    if entrada != 999:
        cont += 1
        soma += entrada

print('Senha Válida!')
print(f'Números de tentativas: {cont}')
print(f'A soma entre os valores informados: {soma}')