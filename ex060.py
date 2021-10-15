opcao = 0
primeiroValor = 0
segundoValor = 0
while opcao != 5:
    opcao = int(input
                ('Escolha uma opção: \n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa '))
    if opcao == 4:
        primeiroValor = float(input('Digite o primeiro valor: '))
        segundoValor = float(input('Digite o segundo valor: '))
    elif opcao == 1:
        print('Resultado da soma: {}'.format(primeiroValor + segundoValor))
    elif opcao == 2:
        print('Resultado da multiplicação: {}'.format(primeiroValor * segundoValor))
    elif opcao == 3:
        if primeiroValor > segundoValor:
            print('{} é o maior número.'.format(primeiroValor))
        elif segundoValor > primeiroValor:
            print('{} é o maior número'.format(segundoValor))
        else:
            print('Os números digitados são iguais.')
