tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número de 0 a 20:'))
if -1 < numero < 21:
    print(f'Você digitou {tupla[numero]}')
else:
    print('Número inválido!')