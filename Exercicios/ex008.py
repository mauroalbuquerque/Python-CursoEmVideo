#conversor de metros para centimetros e milimetros

compr = float(input('\033[4mDigite um valor em metros:\033[m '))

comprm = compr*100
comprmm = compr*1000

print('\033[7:40m{}[m] = {}[cm] = {}[mm]\033[m'.format(compr, comprm, comprmm))
