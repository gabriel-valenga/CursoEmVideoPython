def leiaInt(frase):
    """
    Função que retorna o número inteiro digitado ou se não for inteiro é exibida uma mensagem de erro, e executa novamente a função.
    :param frase: frase de instrução para o usuário digitar um número inteiro
    :return: se não der erro retorna um integer.
    """
    inteiro = input(frase)
    while not inteiro.isdecimal():
        print('ERRO! Não foi passado um número inteiro por parâmetro.')
        inteiro = input(frase)
    return inteiro


numero = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {numero}')
