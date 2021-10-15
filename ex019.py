from math import sqrt,pow
# formula -> a²=b²+c²
catetoOposto = float(input('Digite a medida do cateto oposto: '))
catetoAdjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = sqrt(pow(catetoOposto,2) + pow(catetoAdjacente,2))
print('Comprimento da hipotenusa: {:.2f}'.format(hipotenusa))