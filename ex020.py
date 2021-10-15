from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seno: {:.2f}; Cosseno: {:.2f}; Tangente: {:.2f}'.format(seno, cosseno, tangente))




