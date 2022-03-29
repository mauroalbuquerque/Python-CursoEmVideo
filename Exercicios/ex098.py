from time import sleep

def contador(a, b, c):

    if a < b and c != 0:
        for c in range(a, b + 1, c):
            print(c, end=' ')
            #sleep(.5)

    elif a > b:
        for c in range(a, b - 1, -c):
            print(c, end=' ')
            #sleep(.5)

    elif c <= 0 and a > b:
        for c in range(a, b, -1):
            print(c, end=' ')

    elif c <= 0 and a < b:
        for c in range(a, b, 1):
            print(c, end=' ')

    print()

contador(1, 31, 2)

contador(10, 0, 2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
