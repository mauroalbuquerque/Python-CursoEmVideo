mylist = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('-' * 30)
print('{:^30}'.format('Lista de preços'))
print('-' * 30)

controle = 0

for c in range(0, len(mylist) - 1, 2):
    print('{:.<20}'.format(mylist[c]), 'R$', '{:>7.2f}'.format(mylist[c + 1]))

