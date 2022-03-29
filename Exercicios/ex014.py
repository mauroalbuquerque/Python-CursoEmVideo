#Conversor de temperatura

celcius = float(input('\033[040mInforma a temperatura em °C:\033[m '))

tempf = celcius * 9/5 + 32

print('{} °C = {} °F'.format(celcius, tempf))
