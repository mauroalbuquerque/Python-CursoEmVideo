#Calculadora do Sen, Cos e Tang

from math import radians, cos, sin, tan
angulo = float(input('\033[1:45mDigite um angulo que vc deseja:\033[m '))
seno = sin(radians(angulo))
print('O ângulo de {} = seno {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a tangente  de {:.2f}'.format(angulo, tangente))