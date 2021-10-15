from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0, 100))
    print(lista)


def somaPares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(soma)


lista = []

sorteia(lista)
somaPares(lista)