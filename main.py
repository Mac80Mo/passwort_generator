import verschluesselungs_handler as ver_handler
import passwort_handler as pw_handler

# Lädt den Verschlüsselungsschlüssel aus der Datei
key = ver_handler.load_key()

# Hauptprogramm: Interaktives Menü
print("Willkommen bei diesem Passwort Generator.\nBitte wähle einer der folgenden Optionen aus:")
while True:
    print("1. Neues Passwort erzeugen und speichern")  # Option zur Passwortgenerierung
    print("2. Bestehendes Passwort einlesen")  # Option zur Passwortanzeige
    print("3. Programm beenden")  # Option zum Beenden des Programms
    
    entscheidung = input("Wähle eine Option:")  # Benutzerentscheidung
    
    if entscheidung == "1":
        # Neues Passwort generieren und speichern
        print("Neues Passwort erzeugen und speichern")
        index = input("Wie soll das Passwort referenziert werden? \n")  # Referenzname für das Passwort
        laenge = int(input("Wie lang soll das Passwort sein? \n") or "12")  # Länge des Passworts
        passwort = pw_handler.passwort_erzeugen(laenge)  # Generiert das Passwort
        pw_handler.passwort_speichern(index, passwort, key)  # Speichert das Passwort
        print(f"Passwort für {index} wurde erfolgreich gespeichert")
     
    elif entscheidung == "2":
        # Bestehendes Passwort einlesen
        print("Bestehendes Passwort einlesen")
        index = input("Welches Passwort möchtest Du denn lesen? \n")  # Name des gewünschten Passworts
        passwort = pw_handler.passwort_lesen(index, key)  # Ruft das Passwort ab
        
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
