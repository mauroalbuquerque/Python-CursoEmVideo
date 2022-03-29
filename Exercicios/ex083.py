lista = str(input('Digite a sua expressão: '))

pilha = []

for c in lista:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão nãor é válida!')