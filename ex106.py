def notas(medias, sit=False):
    """
    Função que recebe as médias de uma turma e retorna uma análise sobre esses dados.
    :param medias: um ou mais valores do tipo Float
    :param sit: parâmetro opcional, se for True exibirá também a situação da turma
    :return: tipo dict, retorna um dicionário no formato: {'total': x, 'maior': x, 'menor': x, 'média': x, 'situação': x} (situacao é exibido ou não de acordo com o parâmetro sit)
    """
    maior = menor = cont = soma = 0
    for m in medias:
        num = float(m)
        if cont == 0:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        soma += num
        cont += 1
    mediageral = round((soma / len(medias)), 2)
    if not sit:
        return {'total': soma, 'maior': maior, 'menor': menor, 'média': mediageral}
    else:
        if mediageral <= 3:
            situacao = 'PÉSSIMA'
        elif mediageral <= 5.9:
            situacao = 'RUIM'
        elif mediageral <= 7.9:
            situacao = 'BOA'
        else:
            situacao = 'EXCELENTE'
        return {'total': soma, 'maior': maior, 'menor': menor, 'média': mediageral, 'situação': situacao}


notasTurma = input('Digite as notas da turma:').split(', ')
exibirSituacao = input('Deseja exibir a situação? (S/N)') in 'Ss'
print(notas(notasTurma, exibirSituacao))
