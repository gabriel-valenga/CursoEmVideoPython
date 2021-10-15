lista = list()
maiorPosicoes = list()
menorPosicoes = list()
maiorPosicoesString = menorPosicoesString = ''
maior = menor = posicao = 0
for cont in range(0, 5):
    lista.append(int(input('Digite um número:')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
for numero in lista:
    if lista[posicao] == maior:
        maiorPosicoes.append(posicao)
    if lista[posicao] == menor:
        menorPosicoes.append(posicao)
    posicao += 1
for maiorP in maiorPosicoes:
    maiorPosicoesString += f'{maiorP}'
for menorP in menorPosicoes:
    menorPosicoesString += f'{menorP}'
maiorPosicoesString = ', '.join(maiorPosicoesString)
menorPosicoesString = ', '.join(menorPosicoesString)
print(f'Lista: {lista}. Maior: {maior}, posições: {maiorPosicoesString}. Menor: {menor}, posições {menorPosicoesString}')
