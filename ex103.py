def fatorial(numero, mostrar=False):
    """
    Função para calcular o fatorial do número e retornar o fatorial.
    :param numero: Obrigatório, deve ser um número.
    :param mostrar: Opcional, tipo booleano, valor padrão: False,
                    se passar o valor True para o parâmetro, exibirá o processo de cálculo do fatorial
    :return: fatorial do numero passado.
    """
    fat = numero
    for n in range(numero - 1, 0, -1):
        if mostrar:
            print(f'{fat} * {n} = ', end='')
        fat *= n
        if mostrar:
            print(fat)
    return fat


# help(range)
numeroFatorial = int(input('Digite um número para calcular o fatorial: '))
mostraCalculo = input('Deseja exibir o processo de cálculo do fatorial?') in 'Ss'
print(f'O fatorial de {numeroFatorial} é {fatorial(numeroFatorial, mostraCalculo)}')
#help(fatorial)