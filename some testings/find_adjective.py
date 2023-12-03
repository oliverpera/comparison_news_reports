import spacy
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

nlp = spacy.load("de_core_news_sm")
input_file_name = "article_text.txt"

full_text = ""

with open(input_file_name, 'r') as input_file:
    for line in input_file:
        full_text += line  

doc = nlp(full_text)
adjectives = [token.text for token in doc if token.pos_ == "ADJ"]


tokenizer = RegexpTokenizer(r'\w+') 
all_words = len(tokenizer.tokenize(full_text))

print("Gefilterte Adjektive:", adjectives)
print(len(adjectives) /all_words )
print(len(adjectives))
print(full_text)
