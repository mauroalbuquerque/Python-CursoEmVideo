#Programa de conversão de bases numéricas

num = int(input('Digite um número inteiro: '))

print('1 - Binário / 2 - Octal / 3 - Hexadecimal')
selecao = int(input('Escolha uma das opções acima: '))

if selecao  == 1:
    print('Binário')
    conversao = bin(num)[2:]
elif selecao == 2:
    print('Octal')
    conversao = oct(num)[2:]
elif selecao == 3:
    print('Hexadecimal')
    conversao = hex(num)[2:]
else:
    print('Opção inválida!')
    quit()

print(conversao)
