#Ordem de apresentação dos alunos

from random import shuffle

nome1 = str(input('Digite o nome do primeiro aluno: ').strip())
nome2 = str(input('Digite o nome do outro aluno: ').strip())
nome3 = str(input('Digite o nome do outro aluno: ').strip())
nome4 = str(input('Digite o nome do outro aluno: ').strip())

lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print('\033[45m', lista, '\033[m')
