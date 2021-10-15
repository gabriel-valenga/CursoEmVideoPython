def metade(valor, formatarmoeda=False):
    """
    Função para retornar metade do valor passado por parâmetro
    :param valor: tipo float
    :param formatarmoeda: tipo boolean, padrão false, se passado como true, o retorno será formatado como moeda
    :return: tipo float, retorna o valor, passado no param valor, dividido por 2
    """
    if formatarmoeda:
        return moeda(valor / 2)
    else:
        return valor / 2


def dobro(valor, formatarmoeda=False):
    """
    Função para retornar o dobro do valor passado por parâmetro
    :param valor: tipo float
    :param formatarmoeda: tipo boolean, padrão false, se passado como true retorna o valor formatado como moeda
    :return: tipo float, retorna o valor, passado no param valor, dividido por 2
    """
    if formatarmoeda:
        return moeda(valor * 2)
    else:
        return valor * 2


def aumentar(valor, porcentagem, formatarmoeda=False):
    """
    Função para retornar o valor passado por parãmetro acrescido da porcentagem passada por parâmetro
    :param valor: tipo float
    :param porcentagem: tipo float
    :param formatarmoeda: tipo boolean, padrao false, se passado como true retorna o valor formatado como moeda
    :return: tipo float, retorna o valor passado por parâmetro somado a porcentagem
    """
    if formatarmoeda:
        return moeda(valor + calcularPorcentagem(valor, porcentagem))
    else:
        return valor + calcularPorcentagem(valor, porcentagem)


def diminuir(valor, porcentagem, formatarmoeda=False):
    """
    Função para retornar o valor passado por parâmetro subtraído da porcentagem passada
    :param valor: tipo float
    :param porcentagem: tipo float
    :param formatarmoeda: tipo boolean, padrão false, se passado como true, retorna o valor formatado como moeda
    :return: tipo float, retorna o valor passado por parâmetro subtraído da porcentagem
    """
    if formatarmoeda:
        return moeda(valor - calcularPorcentagem(valor, porcentagem))
    else:
        return valor - calcularPorcentagem(valor, porcentagem)


def calcularPorcentagem(valor, porcentagem):
    """
    Função para calcular a porcentagem a partir do valor informado
    :param valor: tipo float
    :param porcentagem: tipo float
    :return: tipo float, retorna o resultado do cálculo de valor * (porcentagem * 0.01)
    """
    return valor * (porcentagem * 0.01)


def resumoValorMoeda(valor, poraumento=0, porreducao=0):
    """
    Função que retorna um resumo das funções de moeda para o valor passado.
    :param valor: tipo float
    :param poraumento: tipo float, padrão 0, com base nele é calculado o aumento
    :param porreducao: tipo float, padrão 0, com base nele é calculado a redução
    :return: tipo string, retorna um string com o resumo das funções
    """
    resumo = (f'{"-"*30} \n {"Resumo do valor" :^30} \n{"-"*30} \n' +
              f'Preço Analisado: \t{moeda(valor)} \n' +
              f'Dobro do preço: \t{dobro(valor, True)} \n' +
              f'Metade do preço: \t{metade(valor, True)} \n' +
              f'{poraumento :.2f}% de aumento: \t{aumentar(valor, poraumento, True)} \n' +
              f'{porreducao :.2f}% de redução: \t{diminuir(valor, porreducao, True)}')
    return resumo


def moeda(valor):
    return f'R${valor :.2f}'.replace('.', ',')

