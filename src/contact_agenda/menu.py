# src/contact_agenda/menu.py
def show_menu(contact_manager):
    while True:
        print("\n--- AGENDA DE CONTATOS ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            add_contact(contact_manager)
        elif choice == "2":
            list_contacts(contact_manager)
        elif choice == "3":
            search_contact(contact_manager)
        elif choice == "4":
            remove_contact(contact_manager)
        elif choice == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida!")

def add_contact(manager):
    print("\n--- ADICIONAR CONTATO ---")
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    manager.add_contact(name, phone, email)
    print("Contato adicionado com sucesso!")

def list_contacts(manager):
    print("\n--- LISTA DE CONTATOS ---")
    contacts = manager.get_all_contacts()
    for contact in contacts:
        print(f"Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}")

def search_contact(manager):
    print("\n--- BUSCAR CONTATO ---")
    name = input("Digite o nome para buscar: ")
    contact = manager.search_contact(name)
    if contact:
        print(f"Contato encontrado - Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Contato não encontrado!")

def remove_contact(manager):
    print("\n--- REMOVER CONTATO ---")
    name = input("Digite o nome do contato a remover: ")
    if manager.remove_contact(name):
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado!")