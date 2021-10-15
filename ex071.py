nome = continuar = nomeMaisBarato = ''
preco = total = precoMaisBarato = maisDeMil = contador = 0
while True:
    nome = input('Digite o nome do produto:')
    preco = float(input('Digite o preço do produto:'))
    if contador == 0 or preco < precoMaisBarato:
        nomeMaisBarato = nome
        precoMaisBarato = preco
    if preco > 1000:
        maisDeMil += 1
    total += preco
    contador += 1
    while continuar not in ['S', 'N']:
        continuar = input('Deseja Continuar? (S/N)').upper()
    if continuar == 'N':
        break
    continuar = ''
print(f'Total gasto: R${total:.2f}; Produto mais barato: {nomeMaisBarato} = R${precoMaisBarato:.2f}; Quantidade de produtos acima de 1000: {maisDeMil}')
