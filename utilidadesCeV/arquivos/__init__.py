def arquivo_existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        return a.readlines()


def gravar_no_arquivo(arquivo, conteudo):
    try:
        a = open(arquivo, 'at')
        a.write(conteudo)
        a.write('\n')
    except:
        print('Erro ao gravar no arquivo.')


