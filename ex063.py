primeiroTermo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
novosTermos = 0
n = 0
limite = 10
while n < limite:
    print(primeiroTermo)
    primeiroTermo += razao
    n += 1
    if n == limite:
        novosTermos = int(input('Digite quantos termos a mais quer fazer:'))
        if novosTermos != 0:
            limite += novosTermos


