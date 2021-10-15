palavras = ('aprender', 'programar', 'futuro', 'linguagem')
vogais = ('a', 'e', 'i', 'o', 'u')
i = 0
j = 0
vogaisPalavra = ()
for i in range(0, len(palavras)):
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in vogais:
            vogaisPalavra += tuple(palavras[i][j])
    print(f'Na palavra {palavras[i].upper()} temos as vogais: {vogaisPalavra}')
    vogaisPalavra = ()