pessoas = []
somaIdade = 0
mediaIdade = 0
nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0
mulheresSubVinte = 0
for i in range(0, 4):
    pessoa = input('Digite o nome, idade e sexo da pessoa:').split(' ')
    somaIdade += int(pessoa[1])
    if pessoa[2] == 'M' and int(pessoa[1]) > idadeHomemMaisVelho:
        idadeHomemMaisVelho = int(pessoa[1])
        nomeHomemMaisVelho = pessoa[0]
    if pessoa[2] == 'F' and int(pessoa[1]) < 20:
        mulheresSubVinte += 1
    pessoas.append(pessoa)
mediaIdade = somaIdade / len(pessoas)
print('Média de idade do grupo: {}'.format(mediaIdade))
print('Homem mais velho do grupo: {}, idade: {}'.format(nomeHomemMaisVelho, idadeHomemMaisVelho))
print('Quantidade de mulheres abaixo de 20 anos: {}'.format(mulheresSubVinte))
