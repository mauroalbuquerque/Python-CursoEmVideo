#Resolução matematica

num = int(input('Digite um valor entre 0 e 9999: '))

milhar = num // 1000
centena = (num // 100) - milhar * 10
dezena = (num // 10) - centena * 10 - milhar * 100
unidade = (num // 1) - dezena * 10 - centena * 100 - milhar * 1000

print(milhar, centena, dezena, unidade)
