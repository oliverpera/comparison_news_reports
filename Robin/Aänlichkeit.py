from textblob_de import TextBlobDE as TextBlob




input_file_name = "article_text.txt"

input_file_name2 = "second_text.txt"




# Initialisiere den String für den gesamten Text
full_text = ""
full_text2 = ""

# Öffne die Textdatei und lies den Inhalt Zeile für Zeile
with open(input_file_name, 'r') as input_file:
    for line in input_file:
        full_text += line  # Füge die Zeile zum gesamten Text hinzu

with open(input_file_name2, 'r') as input_file:
    for line in input_file:
        full_text2 += line  # Füge die Zeile zum gesamten Text hinzu

# TextBlob-Objekte erstellen
blob1 = TextBlob(full_text)
blob2 = TextBlob(full_text2)

# Ähnlichkeit der Texte berechnen
similarity = blob1.similarity(blob2)

print(f"Ähnlichkeit der Texte: {similarity}")