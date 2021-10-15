from random import randint

numeroDigitado = int(input('Adivinhe o número entre 0 e 5:'))
numeroSorteado = randint(0,5)
print('Você acertou' if numeroDigitado == numeroSorteado else 'Você Errou')
