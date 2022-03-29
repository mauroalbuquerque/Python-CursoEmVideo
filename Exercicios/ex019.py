#Sortei alunos

from random import choice

nome1 = str(input('Digite o nome do seu primeiro aluno: ').strip())
nome2 = str(input('Digite o nome do segundo aluno: ').strip())
nome3 = str(input('Digite o nome do terceiro aluno: ').strip())
nome4 = str(input('Digite o nome do quarto aluno: ').strip())

selecionado = choice([nome1, nome2, nome3, nome4])

print ('O aluno selecionado foi o {}{}{}'.format('\033[41m', selecionado, '\033[m'))
