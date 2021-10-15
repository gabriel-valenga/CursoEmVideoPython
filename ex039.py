numero = int(input('Digite o número a ser convertido:'))
baseNumerica = int(input('Digite a base numérica de conversão (1-binário / 2-octal/ 3-hexadecimal:'))
numeroConvertido = 0
opcaoInvalida = False
if baseNumerica == 1:
    numeroConvertido = bin(numero)
elif baseNumerica == 2:
    numeroConvertido = oct(numero)
elif baseNumerica == 3:
    numeroConvertido = hex(numero)
else:
    opcaoInvalida = True
if not opcaoInvalida:
    print('Número convertido: ' + numeroConvertido)
else:
    print('Opção inválida.')