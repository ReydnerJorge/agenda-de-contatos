# src/contact_agenda/storage.py

import os

CONTACTS_FILE = os.path.join("data", "contacts.txt")

def read_contacts():
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def write_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        f.writelines(contacts)

def append_contact(contact):
    with open(CONTACTS_FILE, "a", encoding="utf-8") as f:
        f.write(contact)
