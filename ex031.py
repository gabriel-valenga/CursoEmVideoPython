velocidade = float(input('Digite a velocidade do carro:'))
if (velocidade > 80):
    print('O carro foi multado. Valor da multa: R${:.2f}'.format((velocidade-80)*7))
