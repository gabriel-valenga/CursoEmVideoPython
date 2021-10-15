valorCasa = float(input('Digite o valor da casa:'))
salarioComprador = float(input('Digite o salário do comprador:'))
anosPagar = float(input("Digite em quantos anos o empréstimo será pago:"))
meses = anosPagar * 12
parcelaMensal = valorCasa / meses
if parcelaMensal > (salarioComprador * 0.30):
    print('Empréstimo negado.')
else:
    print('Empréstimo aceito, valor da parcela mensal: {:.2f}, tempo {} meses.'.format(parcelaMensal, meses))
