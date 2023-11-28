from nltk.tokenize import word_tokenize,sent_tokenize
from textblob_de import TextBlobDE


full_text = ''

input_file_name = "article_text.txt"

with open(input_file_name, 'r') as input_file:
    for line in input_file:
        full_text += line  # Füge die Zeile zum gesamten Text hinzu



word_list = word_tokenize(full_text)

print(len(word_list))


sentences = sent_tokenize(full_text)

print(len(sentences))

subjekt = TextBlobDE(full_text)

print(subjekt.sentiment)

def count_exclamation_marks(text):
    count = text.count('!')
    return count

print(count_exclamation_marks(full_text))