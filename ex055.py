from datetime import date

contador = 0
anoAtual = date.today().year
for i in range(0,7):
    anoNasc = int(input('Digite o ano de nascimento:'))
    if (anoAtual - anoNasc) >= 18:
        contador += 1
print(contador)
