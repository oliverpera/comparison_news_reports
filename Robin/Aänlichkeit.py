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
<<<<<<< HEAD:Robin/Aänlichkeit.py

# TextBlob-Objekte erstellen
blob1 = TextBlob(full_text)
blob2 = TextBlob(full_text2)
    


word_list = full_text.split()
word_list2 = full_text2.split()

word_list = set(word_list)
word_list2 = set(word_list2)


def find_diffrent_words(word_list,word_list2):
    liste = word_list.difference(word_list2)
    liste = list(liste)
    return liste
   



