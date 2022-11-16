# iks-coding-club-python
Unterlagen für den Coding Club bei IKS GmbH


## Installation

1. [Python 3.11](https://www.python.org/downloads/release/python-3110/) herunterladen & installieren
2. Installation testen
   1. Kommandozeile öffnen und dort `python --version` eingeben
3. [Virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) einrichten
   1. Im Root-Verzeichnis des gecloneten Repositories Kommandozeile öffnen
   2. `python -m venv .venv/`
   3. Virtual Environment aktivieren
      1. `.venv/Scripts/activate` (Windows-Kommandozeile)
      2. `source .venv/Scripts/activate` (Git-bash o.ä. Bash-Kommandozeilen)
   4. Überprüfen ob Virtual Environment korrekt aktiviert wurde
      1. `where python` -> Ausgabe sollte Pfad zum Interpreter in `.venv/..` zeigen
3. Paketabhängigkeiten installieren
  - `pip install -r requirements.txt`

## Wie nutze ich dieses Tutorial?

TODO

## Alternative ohne Installation: mybinder.org

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PSteinweg/iks-coding-club-python/HEAD)

Statt die Installation durchzuführen kann alternativ der Online-Service [mybinder](https://mybinder.org/) genutzt werden.
Binder erstellt auf Basis des Repositories automatisch eine Umgebung mit installiertem Python & Abhängigkeiten inkl. Jupyter Notebook, in denen die Jupyter Notebooks ausgeführt werden können


## Nützliche Quellen zum Weiterlernen
- [Crash into Python](https://stephensugden.com/crash_into_python/)

- [Full Stack Python](https://www.fullstackpython.com/)
  - Sehr nützliche Linksammlung, die Python 
- [Real Python](https://realpython.com/)
  - Sammlung von Python Tutorials & Kursen
  - Tutorials eher auf einzelne Python-Themen zugeschnitten, z.B. [Getters and Setters: Manage Attributes in Python](https://realpython.com/preview/python-getter-setter/) oder [https://realpython.com/primer-on-python-decorators/](https://realpython.com/primer-on-python-decorators/)
  
  Nutze ich persönlich sehr gerne um einzelne Dinge wieder "aufzufrischen"
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
  - Handbuch für Python _im täglichen Einsatz_ von Kenneth Reitz (Autor)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/python3/)
  