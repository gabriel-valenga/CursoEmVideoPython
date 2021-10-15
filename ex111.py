from utilidadesCeV import moeda

valor = float(input('Digite um valor:'))
aumento = float(input('Digite um valor para aumento:'))
reducao = float(input('Digite um valor para redução:'))
print(moeda.resumoValorMoeda(valor, aumento, reducao))