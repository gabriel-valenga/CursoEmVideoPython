from random import randint
jogos = numSorteado = 0
jogo = []
numeros = []
jogos = int(input('Digite quantos jogos serão feitos:'))
for i in range(0, jogos):
    for j in range(0, 6):
        numSorteado = randint(1, 60)
        while numSorteado in jogo:
            numSorteado = randint(1, 60)
        jogo.append([numSorteado])
    numeros.append([i, jogo[:]])
    jogo.clear()
for i in range(0, len(numeros)):
    print(f'JOGO {numeros[i][0]+1}')
    print(f'{sorted(numeros[i][1])}')
