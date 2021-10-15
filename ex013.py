precoProduto = float(input('Qual o preço do produto?'))
precoAposDesconto = precoProduto - (precoProduto * 0.05)
print('Preço após 5% de desconto: {:.2f}'.format(precoAposDesconto))