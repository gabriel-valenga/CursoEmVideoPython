aluno = {}
aluno['nome'] = input('Nome:')
aluno['media'] = float(input('Média:'))
if aluno['media'] >= 6:
    aluno['resultado'] = 'APROVADO'
else:
    aluno['resultado'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} = {v}')
