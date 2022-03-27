#Aula de Listas []

num = [2, 5, 9, 1] #Criando uma lista

num[2] = 3 #Alterando o valor de uma lista

num.append(7) #Criando um novo valor no final da lista

num.sort() #Organaliza os valores da lista em ordem
#num.sort(reverse = True) Organiza os valores em ordem decrescente

num.insert(2, 2) #Acrescenta no indíce 2 o valor 2

num.pop(4) #Elimina o item com indice 4 da lista, caso não seja colocado nenhum valor ele irá apagar o ultimo item da lista

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(num)

print(f'Essa lista possui {len(num)} elementos')

#Outros exemplos

'''valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')'''

#Outro exemplo

a = [2, 3, 4, 7]

b = a       #Neste caso o Python cria um ligação entre as 2 listas o que for alterado em uma será alterado também na outra
b[0] = 1

c = a[:]    #Neste caso o Python só repassa os valores de uma lista para a outra não havendo nenhuma ligação entre elas

c[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
