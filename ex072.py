cinquenta = vinte = dez = um = restante = 0
saque = int(input('Qual o valor a ser sacado?'))
restante = saque
while True:
    while restante >= 50:
        restante -= 50
        cinquenta += 1
    while restante >= 20:
        restante -= 20
        vinte += 1
    while restante >= 10:
        restante -= 10
        dez += 1
    while restante >= 1:
        restante -= 1
        um += 1
    if restante == 0:
        break
print(f'Saque de {saque} reais: {cinquenta}x 50, {vinte}x 20, {dez}x 10, {um}x 1')
