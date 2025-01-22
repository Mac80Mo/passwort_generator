# Passwort Generator

Dieses Projekt ist ein modularer, sicherer Passwort-Manager und Generator, der mithilfe der `cryptography`-Bibliothek Passwörter verschlüsselt speichert und entschlüsselt. Der Benutzer kann neue Passwörter generieren, speichern und bestehende Passwörter einlesen.

Das Projekt ist funktional, jedoch gibt es noch Potenzial für Erweiterungen und Verbesserungen.

## Anforderungen
- Python 3.7 oder höher
- Installierte Bibliothek `cryptography`

Installiere die benötigte Bibliothek mit folgendem Befehl:
```bash
pip install cryptography
```

## Funktionen
### 1. Generierung eines Verschlüsselungsschlüssels
Die Funktion `generate_key()` generiert einen sicheren Schlüssel und speichert ihn in der Datei `files/key`. Dies muss nur einmal ausgeführt werden, um den Schlüssel zu erstellen.

### 2. Generierung eines sicheren Passworts
Die Funktion `passwort_erzeugen()` erstellt ein Passwort basierend auf:
- Länge (Standard: 12 Zeichen)
- Optionaler Verwendung von Sonderzeichen

### 3. Verschlüsselung und Speicherung von Passwörtern
- Die Funktion `verschluesseln()` verschlüsselt Passwörter mit dem Fernet-Algorithmus.
- Die Passwörter werden in der Datei `files/passwords` gespeichert. Jedes Passwort wird mit einem Referenznamen versehen.

### 4. Entschlüsselung und Abruf von Passwörtern
Die Funktion `passwort_lesen()` sucht nach einem gespeicherten Passwort basierend auf dem Referenznamen und entschlüsselt es, falls gefunden.

## Ordnerstruktur
Das Projekt verwendet folgende Ordnerstruktur:
```
.
├── files/
│   ├── key            # Enthält den generierten Verschlüsselungsschlüssel
│   ├── passwords      # Speichert die verschlüsselten Passwörter
├── konstanten.py      # Enthält Konfigurationswerte und Pfade
├── main.py            # Startpunkt des Programms
├── passwort_handler.py # Funktionen für Passwort-Management
├── verschluesselungs_handler.py # Funktionen für Schlüssel- und Verschlüsselungslogik
└── README.md          # Dokumentation des Projekts
```

## Nutzung
1. **Generiere den Verschlüsselungsschlüssel (nur einmal):**
   ```python
   from verschluesselungs_handler import generate_key
   generate_key()
   ```

2. **Starte den Passwort-Manager:**
   Führe das Hauptskript aus:
   ```bash
   python main.py
   ```

3. **Menü-Optionen:**
   - **1:** Neues Passwort generieren und speichern
     - Gib den Referenznamen und die gewünschte Länge des Passworts an.
   - **2:** Bestehendes Passwort einlesen
     - Gib den Referenznamen des gespeicherten Passworts ein.
   - **3:** Programm beenden

## Beispielablauf
### Neues Passwort erzeugen und speichern
1. Wähle Option `1`.
2. Gib den Referenznamen (z. B. `twitter.com`) ein.
3. Gib die Länge des Passworts ein (z. B. `16`).
4. Das Passwort wird generiert, verschlüsselt und gespeichert.

### Bestehendes Passwort einlesen
1. Wähle Option `2`.
2. Gib den Referenznamen ein (z. B. `twitter.com`).
3. Das Passwort wird entschlüsselt und angezeigt.

### Programm beenden
Wähle Option `3`, um das Programm zu beenden.

## Sicherheitshinweise
- **Schlüssel sicher aufbewahren:** Die Datei `files/key` ist notwendig, um Passwörter zu entschlüsseln. Geht sie verloren, können die Passwörter nicht wiederhergestellt werden.
- **Passwortdatei schützen:** Bewahre die Datei `files/passwords` an einem sicheren Ort auf.

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz.

