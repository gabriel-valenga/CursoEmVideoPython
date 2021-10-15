numero = 0
numeros = [[], []]
for i in range(0, 7):
    numero = int(input('Digite um número:'))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(f'Números pares: {sorted(numeros[0])}')
print(f'Números ímpares: {sorted(numeros[1])}')
