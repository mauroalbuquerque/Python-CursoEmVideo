from datetime import date

cont = 0

for c in range(0, 7):
    ano = int(input('Informe o ano de nascimento: '))
    if date.today().year - ano >= 18:
        cont += 1

print(cont, 7 - cont)
