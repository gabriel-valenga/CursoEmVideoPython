numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número:')))
    if input('Deseja continuar? (S/N)') not in 'Ss':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(numeros)
print(pares)
print(impares)