num = soma = 0
salario = 945.34
nome = 'Mauro'

print(f'{nome:-^20}')

print(f'{salario:.0f}')

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    soma += num

print(f'A soma vale {soma}')
