# src/contact_agenda/main.py
from contact_agenda.menu import show_menu # type: ignore
from contact_agenda.contact_manager import ContactManager # type: ignore
def main():
    # Inicializa o gerenciador de contatos
    contact_manager = ContactManager()
    
    # Mostra o menu principal
    show_menu(contact_manager)

if __name__ == "__main__":
    main()