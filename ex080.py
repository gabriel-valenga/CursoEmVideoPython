lista = list()
numero = 0
while True:
    numero = int(input('Digite um número:'))
    if numero not in lista:
        lista.append(numero)
    if input('Deseja continuar?') not in 'Ss':
        break
lista.sort()
print(lista)
