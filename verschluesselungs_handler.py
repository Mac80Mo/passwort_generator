from cryptography.fernet import Fernet  # Importiert die Fernet-Bibliothek zur Verschlüsselung
import konstanten

# Funktion zur Generierung eines Verschlüsselungsschlüssels
def generate_key():
    key = Fernet.generate_key()  # Generiert einen sicheren Fernet-Schlüssel
    with open(konstanten.KEY_PATH, "wb") as key_file:  # Speichert den Schlüssel in einer Datei
        key_file.write(key)

# Funktion zum Laden des Verschlüsselungsschlüssels
def load_key():
    with open(konstanten.KEY_PATH, "rb") as key_file:  # Öffnet die Datei im Lesemodus
        return key_file.read()  # Gibt den gespeicherten Schlüssel zurück

# Funktion zur Verschlüsselung einer Nachricht
def verschluesseln(nachricht: str, key):
    fernet_key = Fernet(key)  # Initialisiert das Fernet-Objekt mit dem Schlüssel
    verschluesselte_msg = fernet_key.encrypt(nachricht.encode())  # Verschlüsselt die Nachricht
    return verschluesselte_msg  # Gibt die verschlüsselte Nachricht zurück

# Funktion zur Entschlüsselung einer Nachricht
def entschluesseln(verschluesselte_nachricht, key):
    fernet_key = Fernet(key)  # Initialisiert das Fernet-Objekt mit dem Schlüssel
    nachricht = fernet_key.decrypt(verschluesselte_nachricht).decode()  # Entschlüsselt die Nachricht
    return nachricht  # Gibt die entschlüsselte Nachricht zurück