cont = 1
produtos = ('Pão', 2.50, 'Leite', 1.99, 'Café', 6.99)
tamanhoP1 = tamanhoP2 = 0
print('-' * 30)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        tamanhoP1 = len(produtos[p])
        print(produtos[p], end='')
    else:
        tamanhoP2 = len(f'R$ {produtos[p] :.2f}')
        print('.' * (30 - tamanhoP1 - tamanhoP2) + f'R$ {produtos[p] :.2f}')
print('-' * 30)
