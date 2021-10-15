numero = soma = contador = 0
while numero != 999:
    numero = int(input('Digite um número:'))
    if numero != 999:
        soma += numero
        contador += 1
print('Soma: {}, quantidade de números digitados: {}'.format(soma, contador))
