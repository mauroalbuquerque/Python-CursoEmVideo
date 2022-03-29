maior = 0
menor = 1000000000000000000000

for c in range(0, 5):
    peso = float(input('Informe um peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(maior, menor)
