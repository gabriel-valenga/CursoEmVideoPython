numeros = input('Digite 3 números: ').split(' ')
primeiro = numeros[0]
segundo = numeros[1]
terceiro = numeros[2]
menor = primeiro
maior = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
elif terceiro < primeiro and terceiro < segundo:
    menor = terceiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
elif terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print('Menor número: {}; Maior número: {}.'.format(menor, maior))

