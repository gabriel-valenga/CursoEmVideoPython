lista = list()
numero = 0
for i in range(0, 5):
    numero = int(input('Digite um número:'))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        for c, v in enumerate(lista):
            if numero <= v:
                lista.insert(c, numero)
                break;
print(lista)
