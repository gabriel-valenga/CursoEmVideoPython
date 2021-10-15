def maior(numeros):
    cont = m = 0
    for n in numeros:
        if cont == 0:
            m = n
        else:
            if n > m:
                m = n
        cont += 1
    print(f'O maior número é: {m}')


numeros = input('Digite os números: ').split(' ')
numeros = [int(n) for n in numeros]
maior(numeros)
