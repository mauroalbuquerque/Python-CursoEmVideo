frase = str(input('Digite uma frase qualquer: ').strip())

frase = frase.lower().split()
frase = ''.join(frase)

qtda = frase.count('a')

print(qtda)

print(frase.find('a') + 1, frase.rfind('a') + 1)

print(frase)
