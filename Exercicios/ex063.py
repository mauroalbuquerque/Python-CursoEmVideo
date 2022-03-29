#Sequencia de Fibonacci

cont = a = 0
b = 1

print('Sequencia de Fibonacci')
print('Este programa mostra termos da sequência de Fibonacci')
termos = int(input('Informe quantos termos vc deseja ver: '))

while cont != termos - 2:

    seq = a + b

    if cont == 0:
        print(a, b, end=' ')

    print(seq, end=' ')

    a = b
    b = seq

    cont += 1
