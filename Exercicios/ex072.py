contagem = ('Zero', 'Um', 'Dois', 'Três',
            'Quatro', 'Cinco', 'Seis', 'Sete',
            'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quartoze', 'Quinze', 'Dezesseis',
            'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

selecao = input('Informe um número entre 0 ~ 20: ')

while not int(selecao) >= 0 and int(selecao) <= 20:
    selecao = input('Tente Novamente informando um número válido. Informe um número entre 0 ~ 20: ')

print(selecao)
