# Aufgabe: Skript um .csv in .md-Tabellen umzuwandeln

Gemeinsam wollen wir eine kleines Skript schreiben, welches eine Tabelle im .csv-Format einliest und diese anschließend als .md-Tabelle zurückgibt.

Um euer Programm zu testen liegt im Ordner eine Datei `MOCK_DATA.csv`.

Das Skript soll wie folgt aufrufbar sein: `python -m csv_to_markdown <datei.csv>` und die erzeugte Tabelle anschließend auf der Standardausgabe ausgeben.

## Tipps / Hinweise

- Wir stecken uns die Logik mithilfe bestehender Abhängigkeiten zusammen. Pandas bietet bereits passende Funktionen an: `pd.read_csv()` und `pd.to_markdown()`
- Die übergebenen Argumente stecken in der Liste sys.argv