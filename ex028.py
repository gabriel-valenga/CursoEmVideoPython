frase = str(input('Digite a frase:'))
contadorLetrasA = frase.upper().count('A')
letraAPrimeiraVez = frase.upper().find('A')
letraAUltimaVez = frase.upper().rfind('A')
print('A frase contém {} letras A'.format(contadorLetrasA))
print('Posição em que A aparece pela primeira vez: ' + str(letraAPrimeiraVez))
print('Posição em que A aparece pela última vez: ' + str(letraAUltimaVez))