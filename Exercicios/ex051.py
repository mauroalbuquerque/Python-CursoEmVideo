#Prograssão Artimética

print('Progressão Artimética')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

for c in range(0, 10):
    print(termo, end=' ')
    termo += razao
