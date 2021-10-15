numero = int(input('Digite um número:'))
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        total += 1
if total == 2:
    print('{} é um número primo.'.format(numero))
else:
    print('{} não é um número primo.'.format(numero))
