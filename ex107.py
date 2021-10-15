def pyhelp():
    busca = ''
    while not busca == 0:
        busca = input('Função ou biblioteca: (0 para sair)')
        if busca == '0':
            break
        help(busca)


pyhelp()
