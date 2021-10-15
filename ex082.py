lista = list()
while True:
    numero = lista.append(int(input('Digite um número:')))
    if input('Deseja continuar? (S/N)') not in 'Ss':
        break
print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista.')