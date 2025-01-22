from cryptography.fernet import Fernet  # Importiert die Fernet-Bibliothek zur Verschlüsselung
import secrets  # Modul zur sicheren Erzeugung von Zufallswerten
import string  # Modul zur Verwendung von Zeichenketten (Buchstaben, Zahlen, Sonderzeichen)

# Funktion zur Generierung eines Verschlüsselungsschlüssels
def generate_key():
    key = Fernet.generate_key()  # Generiert einen sicheren Fernet-Schlüssel
    with open("key", "wb") as key_file:  # Speichert den Schlüssel in einer Datei
        key_file.write(key)

# Funktion zum Laden des Verschlüsselungsschlüssels
def load_key():
    with open("key", "rb") as key_file:  # Öffnet die Datei im Lesemodus
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

# Funktion zur Generierung eines sicheren Passworts
def passwort_erzeugen(laenge=12, sonderzeichen=True):
    charaktere = string.ascii_letters + string.digits  # Definiert die Basiszeichen (Buchstaben und Zahlen)
    
    if sonderzeichen:
        charaktere += string.punctuation  # Fügt Sonderzeichen hinzu, wenn aktiviert
        charaktere += "§"  # Fügt das Sonderzeichen "§" hinzu
    
    passwort = ''  # Initialisiert die Passwortvariable
    
    for i in range(laenge):  # Schleife zur Generierung von Zeichen basierend auf der gewünschten Länge
        zufaellig = secrets.choice(charaktere)  # Wählt ein zufälliges Zeichen aus der Zeichenliste
        passwort += zufaellig  # Fügt das zufällige Zeichen zum Passwort hinzu
    
    return passwort  # Gibt das generierte Passwort zurück

# Funktion zum Speichern eines Passworts
def passwort_speichern(index: str, passwort: str, key: bytes):
    ver_passwort = verschluesseln(passwort, key)  # Verschlüsselt das Passwort
    with open("passwords", "ab") as file:  # Öffnet die Passwortdatei im Anhangsmodus
        file.write(index.encode() + b":" + ver_passwort + b"\n")  # Speichert den Index und das verschlüsselte Passwort

# Funktion zum Einlesen eines gespeicherten Passworts
def passwort_lesen(index: str, key: bytes):
    with open("passwords", "rb") as file:  # Öffnet die Passwortdatei im Lesemodus
        for line in file:  # Liest jede Zeile der Datei
            saved_index, ver_passwort = line.strip().split(b":")  # Trennt Index und verschlüsseltes Passwort
            if saved_index.decode() == index:  # Überprüft, ob der Index mit dem gewünschten übereinstimmt
                return entschluesseln(ver_passwort, key)  # Gibt das entschlüsselte Passwort zurück

# Lädt den Verschlüsselungsschlüssel aus der Datei
key = load_key()

# Hauptprogramm: Interaktives Menü
print("Willkommen bei diesem Passwort Generator.\nBitte waehle einer der folgenden Optionen aus:")
while True:
    print("1. Neues Passwort erzeugen und speichern")  # Option zur Passwortgenerierung
    print("2. Bestehendes Passwort einlesen")  # Option zur Passwortanzeige
    print("3. Programm beenden")  # Option zum Beenden des Programms
    
    entscheidung = input("Waehle eine Option:")  # Benutzerentscheidung
    
    if entscheidung == "1":
        # Neues Passwort generieren und speichern
        print("Neues Passwort erzeugen und speichern")
        index = input("Wie soll das Passwort referenziert werden? \n")  # Referenzname für das Passwort
        laenge = int(input("Wie lang soll das Passwort sein? \n") or "12")  # Länge des Passworts
        passwort = passwort_erzeugen(laenge)  # Generiert das Passwort
        passwort_speichern(index, passwort, key)  # Speichert das Passwort
        print(f"Passwort für {index} wurde erfolgreich gespeichert")
     
    elif entscheidung == "2":
        # Bestehendes Passwort einlesen
        print("Bestehendes Passwort einlesen")
        index = input("Welches Passwort möchtest Du denn lesen? \n")  # Name des gewünschten Passworts
        passwort = passwort_lesen(index, key)  # Ruft das Passwort ab
        
        if passwort:
            print(f"Dein Passwort für {index}: {passwort}")  # Zeigt das Passwort an
        else:
            print(f"Passwort konnte für {index} nicht gefunden werden")  # Fehlermeldung bei Nichtauffinden
      
    elif entscheidung == "3":
        # Programm beenden
        print("Programm beendet")
        break  # Beendet die Schleife und das Programm
        
    else:
        # Ungültige Eingabe
        print("Wähle einer der möglichen Optionen = (1, 2, 3)!")
