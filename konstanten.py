import os

# Basisverzeichnis relativ zur Datei konstanten.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Unterverzeichnisse und Dateinamen
MAINDIRECTORY_PATH = "files"
PASSWORT_SUBPATH = "passwords"
KEY_SUBPATH = "key"

# Absolute Pfade
KEY_PATH = os.path.join(BASE_DIR, MAINDIRECTORY_PATH, KEY_SUBPATH)
PASSWORT_PATH = os.path.join(BASE_DIR, MAINDIRECTORY_PATH, PASSWORT_SUBPATH)
