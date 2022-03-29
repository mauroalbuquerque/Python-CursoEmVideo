salario = float(input('Qual é o seu salário: R$ ').strip())

aumento = (salario * 1.10 if salario > 1250 else salario * 1.15)

print(aumento)