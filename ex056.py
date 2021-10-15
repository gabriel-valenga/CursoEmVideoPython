menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa:'.format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('Menor peso: {}Kg. Maior peso: {}Kg'.format(menor, maior))
