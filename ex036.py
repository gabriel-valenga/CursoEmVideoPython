salario = float(input('Digite o salário do funcionário: '))
if (salario > 1250):
    salario += salario * 0.10
else:
    salario += salario * 0.15

print('O salario do funcionário após o aumento: {:.2f}'.format(salario))