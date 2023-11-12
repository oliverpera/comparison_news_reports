import spacy
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

# Laden des deutschen spaCy-Modells
nlp = spacy.load("de_core_news_sm")


input_file_name = "article_text.txt"




# Initialisiere den String für den gesamten Text
full_text = ""

# Öffne die Textdatei und lies den Inhalt Zeile für Zeile
with open(input_file_name, 'r') as input_file:
    for line in input_file:
        full_text += line  # Füge die Zeile zum gesamten Text hinzu

# Analysieren des Texts mit spaCy
doc = nlp(full_text)

# Filtern der Adjektive
adjectives = [token.text for token in doc if token.pos_ == "ADJ"]


tokenizer = RegexpTokenizer(r'\w+') 
all_words = len(tokenizer.tokenize(full_text))
# Ausgabe der gefilterten Adjektive
print("Gefilterte Adjektive:", adjectives)
print(len(adjectives) /all_words )
print(len(adjectives))
#for token in doc:
    #print(token.pos_)
    #print(token)
print(full_text)
