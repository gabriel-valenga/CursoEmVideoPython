from utilidadesCeV import moeda

valor = float(input('Digite um valor:'))
formatarmoeda = input('Deseja formatar o valor como moeda?') in 'Ss'
print(f'A metade do valor é: {moeda.metade(valor, formatarmoeda)}')
print(f'O dobro do valor é: {moeda.dobro(valor, formatarmoeda)}')
print(f'O valor aumentado em 10% é: {moeda.aumentar(valor, 10, formatarmoeda)}')
print(f'O valor diminuído em 35% é: {moeda.diminuir(valor, 35, formatarmoeda)}')