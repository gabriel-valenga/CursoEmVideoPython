def escreva(frase):
    tamanho = len(frase)
    centralizacao = len('~~' * tamanho)
    print('~~' * tamanho)
    print(f'{frase:^{centralizacao}}')
    print('~~' * tamanho)
escreva(input('Digite uma frase: '))