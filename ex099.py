def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    passo = abs(passo)
    if fim < inicio:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        print(i)


inicio = fim = passo = 0

contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Digite o valor de inicio: '))
fim = int(input('Digite o valor de fim: '))
passo = int(input('Digite o valor de passo: '))
contador(inicio, fim, passo)
