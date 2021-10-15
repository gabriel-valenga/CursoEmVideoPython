precoNormal = float(input('Digite o preço normal do produto: '))
condicaoPagamento = input('Digite a condição de pagamento: ')
precoVenda = 0
if condicaoPagamento == 'vista-dinheiro' or condicaoPagamento == 'vista-cheque':
    precoVenda = precoNormal - (precoNormal * 0.10)
elif condicaoPagamento == 'vista-cartão':
    precoVenda = precoNormal - (precoNormal * 0.05)
elif condicaoPagamento == '2x-cartão':
    precoVenda = precoNormal
else:
    precoVenda = precoNormal + (precoNormal * 0.20)
print('Preço total venda: {:.2f}'.format(precoVenda))
