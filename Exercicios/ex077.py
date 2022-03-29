mylist = ('Aprender', 'Fazer', 'Comer', 'Digitar', 'Assistir')

c = cont = 0

while c < len(mylist):
    print('Na palavra {} temos as seguintes vogais:'.format(mylist[c]), end=' ')

    palavra_atual = mylist[c]

    for cont in range(0, len(palavra_atual)):
        if palavra_atual[cont] in 'a e i o u':
            print(palavra_atual[cont], end=' ')
    print('')
    c += 1