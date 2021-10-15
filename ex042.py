idade = int(input('Digite sua idade:'))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUVENIL')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
