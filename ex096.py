jogador = {}
jogadores = []
partidas = []
totalGols = 0
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['numPartidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, jogador['numPartidas']):
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {p}?')))
    jogador['partidas'] = partidas[:]
    for gol in partidas:
        totalGols += gol
    jogador['totalGols'] = totalGols
    jogadores.append(jogador.copy())
    totalGols = 0
    partidas.clear()
    if input('Deseja continuar? ') not in 'Ss':
        break
for p in ['cod', 'nome', 'gols', 'total']:
    print(f'{p:<15}', end='')
print()
print('='*80)
for c, v in enumerate(jogadores):
    print(f'{c}{str(v["nome"]):^20}{str(v["partidas"]):^20}{str(v["totalGols"]):^20}')
while True:
    busca = int(input("Digite o id do jogador que deseja fazer a busca: (999 para sair)" ))
    if busca == 999:
        break
    print(jogadores[busca])


