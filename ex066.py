numero = contador = maior = menor = media = soma = 0
continuar = True
while continuar == True:
    contador += 1
    numero = float(input('Digite o número:'))
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    soma += numero
    continuar = input('Deseja continuar? (S/N)').upper() == 'S'
media = soma / contador
print('Maior: {}; Menor: {}; Média: {:.2f}'.format(maior, menor, media))
