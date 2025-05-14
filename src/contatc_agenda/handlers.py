# src/contact_agenda/handlers.py

from contact_agenda.storage import ( # type: ignore
    read_contacts,
    write_contacts,
    append_contact
)

def add_contact():
    contact_id = input("Enter contact ID: ")
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")

    contact = f"{contact_id};{name};{phone};{email}\n"
    try:
        append_contact(contact)
        print("✅ Contact saved successfully!")
    except Exception as e:
        print(f"❌ Error saving contact: {e}")

def list_contacts():
    contacts = read_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\n📒 Contact list:")
    for contact in contacts:
        print(contact.strip())

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").lower()
    contacts = read_contacts()

    updated_contacts = [
        contact for contact in contacts if name_to_delete not in contact.lower()
    ]

    write_contacts(updated_contacts)
    print("🗑️ Contact deleted successfully.")

def search_contact():
    search_name = input("Enter the name to search: ").lower()
    contacts = read_contacts()

    found = [
        contact for contact in contacts if search_name in contact.split(";")[1].lower()
    ]

    if found:
        print("\n🔍 Found contacts:")
        for contact in found:
            print(contact.strip())
    else:
        print("❌ No contacts found.")

def exit_program():
    print("👋 Goodbye!")
    exit()
