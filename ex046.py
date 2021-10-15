from random import choice

opcaoJogador = input('Pedra, Papel, Tesoura?')
opcaoComputador = choice(['Pedra', 'Papel', 'Tesoura'])
if opcaoJogador == opcaoComputador:
    print('Empate')
elif (opcaoJogador == 'Pedra' and opcaoComputador == 'Tesoura') or (opcaoJogador == 'Tesoura' and opcaoComputador == 'Papel') or (opcaoJogador == 'Papel' and opcaoComputador == 'Pedra'):
    print('Jogador venceu. {} vence {}'.format(opcaoJogador, opcaoComputador))
else:
    print('Computador venceu. {} vence {}'.format(opcaoComputador, opcaoJogador))