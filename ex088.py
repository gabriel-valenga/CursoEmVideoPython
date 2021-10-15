matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = maiorSegundaLinha = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input('Digite um número:'))
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if j == 2:
            somaTerceiraColuna += matriz[i][j]
        if i == 1:
            if j == 0:
                maiorSegundaLinha = matriz[i][j]
            else:
                if matriz[i][j] > maiorSegundaLinha:
                    maiorSegundaLinha = matriz[i][j]
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print(f'Maior segunda linha: {maiorSegundaLinha}')
print(f'Soma terceira coluna: {somaTerceiraColuna}')
