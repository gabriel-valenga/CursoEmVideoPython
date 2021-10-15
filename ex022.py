from random import shuffle

primeiroAluno = str(input('Digite o nome do primeiro aluno:'))
segundoAluno = str(input('Digite o nome do segundo aluno:'))
terceiroAluno = str(input('Digite o nome do terceiro aluno:'))
quartoAluno = str(input('Digite o nome do quarto aluno:'))

listaAlunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(listaAlunos)

print('A ordem será:')
print(listaAlunos)