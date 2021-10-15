from utilidadesCeV import moeda

valor = float(input('Digite o valor: R$'))
print(f'A metade do valor é: {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro do valor é: {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumentar(valor, 10))}')