expressao = str(input('Digite uma expressão:'))
abreParenteses = fechaParenteses = 0
invalida = abriu = False
for c in range(0, len(expressao)):
    if expressao[c] == '(':
        abreParenteses += 1
        abriu = True
    if expressao[c] == ')':
        if abriu == False:
            invalida = True
            break
        fechaParenteses += 1
        abriu = False
if (abreParenteses + fechaParenteses) % 2 != 0:
    invalida = True
if invalida:
    print('Expressão inválida!')