from utilidadesCeV import moeda

valor = float(input('Digite um valor:'))
print(f'A metade do valor é: {moeda.metade(valor)}')
print(f'O dobro do valor é: {moeda.dobro(valor)} ')
print(f'O valor aumentado em 10% é: {moeda.aumentar(valor, 10)}')
print(f'O valor reduzido em 13% é: {moeda.diminuir(valor, 13)}')