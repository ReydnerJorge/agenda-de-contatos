from agenda.operacoes import ( # type: ignore
    cadastrar_contato,
    listar_contatos,
    deletar_contato,
    buscar_contato,
    sair
)

def exibir_menu():
    while True:
        opcao = input('''
    ===============================================
                    PROJETO AGENDA                 
    MENU:

    [1] CADASTRAR CONTATO
    [2] LISTAR CONTATOS
    [3] DELETAR CONTATO
    [4] BUSCAR CONTATO
    [5] SAIR
    ================================================
    ESCOLHA UMA OPÇÃO ACIMA: 
    ''')
        match opcao:
            case "1": cadastrar_contato()
            case "2": listar_contatos()
            case "3": deletar_contato()
            case "4": buscar_contato()
            case "5": sair()
            case _: print("Opção inválida!")

        voltar = input("Deseja voltar ao menu principal? (s/n): ").lower()
        if voltar != 's':
            sair()
