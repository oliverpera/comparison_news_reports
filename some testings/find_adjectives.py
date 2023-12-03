from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
import nltk
from nltk import word_tokenize, pos_tag

text = ""
input_file_name = "article_text.txt"
with open(input_file_name, 'r') as input_file:
    for line in input_file:
        text += line 

def get_number_of_words(text):
    
    tokenizer = RegexpTokenizer(r'\w+')    
    tokens = tokenizer.tokenize(text)

    return(len(tokens))

def get_number_of_adjectives(text):

    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    
    adjectives = [word for word, tag in tagged_words if tag in ["JJ"]]
    
    return(len(adjectives))

def get_most_common_words(text):
    fdist = FreqDist(text)
    return(fdist.most_common(10))

print("Adjective Ratio:", get_number_of_adjectives(text) / get_number_of_words(text))
print(get_most_common_words(text))
words = word_tokenize(text)
tagged_words = pos_tag(words)
adjectives = [word for word, tag in tagged_words if tag in ['JJ']]
print(adjectives)

nltk.download('punkt')  
pos_tags = pos_tag(words)

adjectives = [word for word, pos in pos_tags if pos == "JJ"]
print("Adjektive:", adjectives)