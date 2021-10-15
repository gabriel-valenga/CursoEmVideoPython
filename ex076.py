pares = 0
tupla = tuple(input('Digite quatro valores: ').split(' '))
numeroNove = tupla.count('9')
if '3' in tupla:
    numeroTresFrase = f'O Número 3 apareceu pela primeira vez na posição {tupla.index("3")}.'
else:
    numeroTresFrase = 'O número 3 não apareceu em nenhuma posição.'
for n in tupla:
    if int(n) % 2 == 0:
        pares += 1
print(f'Tupla: {tupla}. Número 9 foi digitado {numeroNove} vezes. {numeroTresFrase} Quantidade números pares: {pares}')
