nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO - MÉDIA: {:.1f}'.format(media))
elif 5.0 < media < 7.0:
    print('RECUPERAÇÃO - MÉDIA: {:.1f}'.format(media))
else:
    print('APROVADO - MÉDIA: {:.1f}'.format(media))