tabelaBrasileirao = ('Atlético Mineiro', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Fluminense', 'Cuiabá', 'Internacional', 'Atlético Goianiense', 'Athletico Paranaense', 'Ceará', 'Santos', 'Juventude', 'Bahia', 'São Paulo', 'América Mineiro', 'Grêmio', 'Sport Recife', 'Chapecoense')
print(f'Cinco primeiros colocados: {tabelaBrasileirao[0:5]}')
print(f'Quatro últimos colocados: {tabelaBrasileirao[-4:]}')
print(f'Em ordem alfabética: {sorted(tabelaBrasileirao)}')
print(f'Posição Chapecoense: {tabelaBrasileirao.index("Chapecoense") + 1}')

