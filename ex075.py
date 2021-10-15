from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor = maior = cont = 0
for n in numeros:
    if cont == 0:
        menor = n
        maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    cont += 1
print(f'Tupla gerada: {numeros}. Menor valor: {menor}. Maior valor: {maior}.')
