from utilidadesCeV.arquivos import *


def menu_principal():
    opcao = 0
    while not opcao == 3:
        print(f'{"-"*40} \n {"MENU PRINCIPAL" :^40}\n{"-"*40}')
        try:
            opcao = int(input(f'1 - ver pessoas cadastradas \n2 - Cadastrar nova pessoa \n3 - Sair \n'))
            if opcao == 1:
                listar_pessoas()
            elif opcao == 2:
                nome = input('Digite o nome da pessoa: ')
                idade = int(input('Digite a idade da pessoa:'))
                adicionar_pessoa(nome, idade)
            elif opcao == 3:
                break
        except (ValueError, TypeError):
            print('Ocorreu um erro na leitura, digite um número novamente.')


def listar_pessoas():
    print(f'{"-" * 40} \n {"PESSOAS CADASTRADAS" :^40}\n{"-" * 40}')
    try:
        for linha in ler_arquivo(arquivo):
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except:
        print('Ocorreu um erro ao listar as pessoasCadastradas')


def adicionar_pessoa(nome, idade):
    try:
        gravar_no_arquivo(arquivo, f'{nome};{idade}')
    except:
        print('Ocorreu um erro ao adicionar a pessoa')


arquivo = 'cursoemvideo.txt'
if arquivo_existe(arquivo):
    print('Arquivo encontrado.')
else:
    print('Arquivo não encontrado.')
    criar_arquivo(arquivo)

menu_principal()
