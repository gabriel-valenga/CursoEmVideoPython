def fichaJogador(nome='desconhecido', gols=0):
    """
    Função que retorna o nome do jogador e quantos gols ele fez.
    :param nome: string que recebe o nome do jogador
    :param gols: int que recebe quantos gols o jogador fez
    :return: string no formato: 'O jogador fez x gols'.
    """
    return f'O jogador {nome} fez {gols} gols.'


jogador = []
jogador = input('Digite as informações do jogador: ').split(' ')
if len(jogador) == 1:
    if jogador[0].isnumeric():
        print(fichaJogador(gols=int(jogador[0])))
    else:
        if len(jogador[0]):
            print(fichaJogador(jogador[0]))
        else:
            print(fichaJogador())
elif len(jogador) == 2:
    if not jogador[1].isnumeric():
        print(fichaJogador(jogador[0]))
    else:
        print(fichaJogador(jogador[0], jogador[1]))

