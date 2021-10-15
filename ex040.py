idade = int(input("Digite sua idade:"))
if idade < 18:
    print('Você vai ter que se alistar daqui {} ano(s).'.format(18 - idade))
elif idade == 18:
    print('Está na hora de você se alistar.')
else:
    print('Você se alistou há {} anos.'.format(idade - 18))