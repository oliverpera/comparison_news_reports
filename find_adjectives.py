from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

def get_number_of_words(text):
    
    tokenizer = RegexpTokenizer(r'\w+')    
    tokens = tokenizer.tokenize(text)

    return(len(tokens))


def get_number_of_adjectives(text):

    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    
    adjectives = [word for word, tag in tagged_words if tag in ['NN', 'NNR', 'NNS']]
    
    return(len(adjectives))


def get_most_common_words(text):
    fdist = FreqDist(text)
    return(fdist.most_common(10))


text = "Das is mir egal und dir? He was soll das denn?"
print("Adjective Ratio:", get_number_of_adjectives(text) / get_number_of_words(text))
print(get_most_common_words(text))

