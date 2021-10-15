quantidadeKm = float(input('Qual a quantidade de km percorridos? '))
quantidadeDias = int(input('Por quantos dias foi alugado? '))
precoPagar = (quantidadeKm * 0.15) + (quantidadeDias * 60)
print('Preço do aluguel do veículo: {}'.format(precoPagar))
