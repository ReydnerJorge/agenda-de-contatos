# /home/reydner96/agenda-de-contatos/agenda-de-contatos/run.py
import sys
import os

# Adiciona src ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.contact_agenda.main import main

if __name__ == "__main__":
    main()