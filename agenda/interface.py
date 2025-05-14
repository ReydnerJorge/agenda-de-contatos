from agenda.contato import buscarContato, cadastrarContato, deletarContato, listarContato, sair

def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''
    ===============================================
                    PROJETO AGENDA                 
    MENU:

    [1]CADASTRA CONTATO
    [2]LISTAR CONTATO
    [3]DELETAR CONTATO
    [4]BUSCAR CONTATO
    [5]SAIR
    ================================================
    ESCOLHA UMA OPÇÃO ACIMA: 
    ''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContato()
        elif opcao == "5":
            sair()
        else:
            print('Opção Inválida!')
        voltaMenuPrincipal = input('Deseja voltar ao menu principal? (s/n) ').lower()
