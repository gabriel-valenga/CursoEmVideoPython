from random import randint, choice

escolhaJogador = escolhaComputador = respostaCerta = ''
numeroJogador = numeroComputador = acertos = 0
while True:
    escolhaJogador = input('Par ou ímpar?').upper()
    numeroJogador = int(input('Digite um número:'))
    escolhaComputador = choice(['PAR', 'ÍMPAR'])
    numeroComputador = randint(0, 10)
    if (numeroJogador + numeroComputador) % 2 == 0:
        respostaCerta = 'PAR'
    else:
        respostaCerta = 'ÍMPAR'
    print(f'Jogador jogou {numeroJogador} e computador jogou: {numeroComputador}')
    if escolhaJogador == respostaCerta:
        print('Jogador venceu a rodada.')
        acertos += 1
    else:
        break
print(f'FIM DE JOGO. QUANTIDADE DE ACERTOS: {acertos}')
