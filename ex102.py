def voto(idade):
    """
    Função para verificação do tipo de voto baseado na idade informada.
    :param idade: obrigatório, deve ser um número.
    :return: retorna uma string:
    - Se idade é maior ou igual a 16 e menor que 18, ou maior ou igual a 80 retorna: 'Voto Opcional.'.
    - Se idade é menor do que 16 retorna 'Voto negado.'.
    - Senão retorna 'Voto Obrigatório.'.
    """
    if (16 <= idade < 18) or (idade >= 65):
        return 'Voto Opcional.'
    elif (idade < 16):
        return 'Voto Negado.'
    else:
        return 'Voto Obrigatório.'


idadePessoa = int(input('Digite sua idade: '))
print(f'Idade: {idadePessoa}. {voto(idadePessoa)}')