from random import randint
player = {}
resultados = []
for i in range(0, 4):
    player = {'jogador': f'PLAYER{i+1}',
              'resultado': randint(1, 6)
              }
    resultados.append(player.copy())
for player in resultados:
        print(f'O jogador {player["jogador"]} tirou {player["resultado"]}')
resultados.sort(key=lambda player: player['resultado'], reverse=True)
for r, p in enumerate(resultados):
    print(f'{r+1}º lugar - {p["jogador"]}')

