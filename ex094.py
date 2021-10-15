jogador = {}
partidas = []
totalGols = 0
jogador['nome'] = input('Digite o nome do jogador:')
jogador['numPartidas'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))
for p in range(0, jogador['numPartidas']):
    partidas.append(int(input(f'Quantos gols o jogador fez na partida {p}?')))
jogador['partidas'] = partidas[:]
for gols in jogador['partidas']:
    totalGols += gols
print(f'O jogador {jogador["nome"]} fez {totalGols} gols.')
for id, gols in enumerate(jogador['partidas']):
    print(f'Na partida {id} o {jogador["nome"]} fez {gols} gols')
