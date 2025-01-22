import secrets  # Modul zur sicheren Erzeugung von Zufallswerten
import string  # Modul zur Verwendung von Zeichenketten (Buchstaben, Zahlen, Sonderzeichen)
import verschluesselungs_handler as ver_handler
import konstanten

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
    ver_passwort = ver_handler.verschluesseln(passwort, key)  # Verschlüsselt das Passwort
    with open(konstanten.PASSWORT_PATH, "ab") as file:  # Öffnet die Passwortdatei im Anhangsmodus
        file.write(index.encode() + b":" + ver_passwort + b"\n")  # Speichert den Index und das verschlüsselte Passwort

# Funktion zum Einlesen eines gespeicherten Passworts
def passwort_lesen(index: str, key: bytes):
    with open(konstanten.PASSWORT_PATH, "rb") as file:  # Öffnet die Passwortdatei im Lesemodus
        for line in file:  # Liest jede Zeile der Datei
            saved_index, ver_passwort = line.strip().split(b":")  # Trennt Index und verschlüsseltes Passwort
            if saved_index.decode() == index:  # Überprüft, ob der Index mit dem gewünschten übereinstimmt
                return ver_handler.entschluesseln(ver_passwort, key)  # Gibt das entschlüsselte Passwort zurück