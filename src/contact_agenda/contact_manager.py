# src/contact_agenda/contact_manager.py
import json
import os

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def _save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f)

    def add_contact(self, name, phone, email):
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })
        self._save_contacts()

    def get_all_contacts(self):
        return self.contacts.copy()

    def search_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None

    def remove_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact["name"].lower() == name.lower():
                del self.contacts[i]
                self._save_contacts()
                return True
        return False