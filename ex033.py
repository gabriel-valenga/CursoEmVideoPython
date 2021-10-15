distanciaViagem = float(input('Digite a distância da viagem em KM: '))
preco = 0.00
if (distanciaViagem <= 200):
    preco = distanciaViagem * 0.50
else:
    preco = distanciaViagem * 0.45
print('Preço da viagem: R${:.2f}'.format(preco))