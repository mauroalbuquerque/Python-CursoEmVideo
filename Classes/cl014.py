num = 1
par = impar = 0

while num != 0:
    num = int(input('Digite um valor '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

print(par, impar)
