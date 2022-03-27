frase = 'Curso em Video Python'

print(frase[9:21:2]) #Vai imprimir do V até o final da frase pulando de caracteres

print(len(frase)) #Vai informar o 'comprimento' da frase

print(frase.count('o', 0, 14)) #Vai contar a quantidade de 'o' que a frase possui

print(frase.find('deo'))

print('Curso' in frase)

frase.replace('Python', 'Android')

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print(frase.split())

meunome = ['Mauro', 'Sergio', 'Albuquerque', 'Santos']
print(' '.join(meunome))