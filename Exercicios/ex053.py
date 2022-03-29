#Verificador de palindromos
#TENET
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA

frase1 = str(input('Digite uma palavra ou frase: ').strip().lower())
frase1 = frase1.replace(' ', '')

resultado = 0

tamanho = len(frase1)

for c in range(tamanho, 0, -1):
    if frase1[c -1] == frase1[tamanho - c]:
        resultado += 1

if resultado == tamanho:
    print('Está frase ou palavra é um palindromo')
else:
    print('Está frase ou palavra não é um palindromo')
