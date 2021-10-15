from math import trunc

numero = float(input('Digite o número:'))
apenasParteInteira = trunc(numero)
print('Parte inteira de {} é {}'.format(numero,apenasParteInteira))