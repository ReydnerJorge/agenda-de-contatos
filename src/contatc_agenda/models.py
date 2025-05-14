# src/contact_agenda/models.py

from dataclasses import dataclass

@dataclass
class Contact:
    contact_id: str
    name: str
    phone: str
    email: str

    def to_line(self) -> str:
        """Converte o objeto Contact para uma linha formatada para salvar no arquivo."""
        return f"{self.contact_id};{self.name};{self.phone};{self.email}\n"

    @staticmethod
    def from_line(line: str):
        """Cria um objeto Contact a partir de uma linha do arquivo."""
        parts = line.strip().split(";")
        if len(parts) != 4:
            raise ValueError(f"Linha inválida: {line}")
        return Contact(*parts)
