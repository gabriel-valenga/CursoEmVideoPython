listaPessoas = []
maisPesadas = []
maisLeves = []
contador = peso = 0
nome = ''
while True:
    nome = input('Digite o nome da pessoa:')
    peso = float(input('Digite o peso da pessoa:'))
    listaPessoas.append([nome, peso])
    if contador == 0:
        maisLeves.append([nome, peso])
        maisPesadas.append([nome, peso])
    else:
        if peso > maisPesadas[0][1]:
            maisPesadas.clear()
            maisPesadas.append([nome, peso])
        elif peso == maisPesadas[0][1]:
            maisPesadas.append([nome, peso])
        if peso < maisLeves[0][1]:
            maisLeves.clear()
            maisLeves.append([nome, peso])
        elif peso == maisLeves[0][1]:
            maisLeves.append([nome, peso])
    if input('Deseja continuar?') not in 'Ss':
        break
    contador += 1
print(f'{len(listaPessoas)} pessoas cadastradas.')
print(f'Pessoas mais leves: {maisLeves}')
print(f'Pessoas mais pesadas: {maisPesadas}')
