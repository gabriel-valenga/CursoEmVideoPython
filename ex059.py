from random import randint

respostaUsuario = -1
respostaCPU = randint(0, 10)
contador = 0
while respostaUsuario != respostaCPU:
    respostaUsuario = int(input('Digite um número de 0 a 10:'))
    contador += 1
print('Você acertou depois de {} tentativa(s)'.format(contador))
