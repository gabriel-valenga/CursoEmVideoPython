pessoas = []
pessoa = {}
mulher = {}
mulheres = []
mediaIdade = somaIdade = 0
acimaDaMedia = []
while True:
    pessoa['nome'] = input('Digite o nome da pessoa:')
    pessoa['sexo'] = input('Digite o sexo da pessoa:')
    pessoa['idade'] = int(input('Digite a idade da pessoa:'))
    pessoas.append(pessoa.copy())
    if input('Deseja continuar?') not in 'Ss':
        break
for p in pessoas:
    somaIdade += p['idade']
    if p['sexo'] in 'Ff':
        mulher = p.copy()
        mulher.pop('sexo')
        mulheres.append(mulher)
mediaIdade = somaIdade / len(pessoas)
for p in pessoas:
    if p['idade'] > mediaIdade:
        acimaDaMedia.append(p.copy())
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade do grupo é {mediaIdade}')
print(f'Mulheres do grupo: {mulheres}')
print(f'Pessoas com idade acima da média: {acimaDaMedia}')
