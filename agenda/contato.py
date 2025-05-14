def cadastrarContato():
    idContato = input('Escolha o ID do Contato: ')
    nome = input('Escreva o nome do Contato: ')
    telefone = input('Escreva o telefone do contato: ')
    email = input('Escreva o email do contato: ')
    try:
        agenda = open('agenda.txt','a')
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!')
    except:
        print('ERRO na gravação do contato')

def listarContato():
    agenda = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    contatoDeletado = input('Digite o nome do contato a ser deletado: ').lower()
    agenda = open('agenda.txt','r')
    aux = []
    aux2 =[]
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if contatoDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt','w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso')
    listarContato()
    
def buscarContato():
    nome = input(f'Digite o nome do contato: ').upper()
    agenda = open('agenda.txt','r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)
    agenda.close()

def sair():
    print(f'Até mais...')
    exit()