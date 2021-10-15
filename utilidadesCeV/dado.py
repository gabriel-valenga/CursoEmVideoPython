from utilidadesCeV import moeda


def leiaInt(frase):
    try:
        numero = int(input(frase))
    except ValueError:
        print('O valor digitado não é um número inteiro')
    else:
        return numero


def leiaFloat(frase):
    try:
        numero = float(input(frase))
    except ValueError:
        print('O valor digitado não é um número float')
    else:
        return numero
def leiaDinheiro(frase):
    """

    :param valor:
    :return:
    """
    invalido = True
    while invalido:
        valor = input(frase).replace(',', '.')
        if valor.isalpha():
            print('ERRO')
        else:
            valor = float(valor)
            return moeda.moeda(valor)
