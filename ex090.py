alunos = []
nome = ''
n1 = n2 = id = idPesquisa = media = 0
while True:
    nome = input('Nome:')
    n1 = float(input('Primeira nota:'))
    n2 = float(input('Segunda nota:'))
    media = (n1 + n2) / 2
    media = round(media, 1)
    alunos.append([id, nome, [n1, n2], media])
    id += 1
    if input('Quer continuar? (S/N)') not in 'Ss':
        break
print('ID   NOME       MÉDIA')
print('='*30)
for c, v in enumerate(alunos):
    print(f'{v[0]}   {v[1]:<10}   {v[3]}')
print('='*30)
while True:
    idPesquisa = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if idPesquisa == 999:
        break
    else:
        if idPesquisa < len(alunos):
            print(f'Notas de {alunos[idPesquisa][1]} são {alunos[idPesquisa][2]} ')
        else:
            print(f'ID {idPesquisa} é inválido.')