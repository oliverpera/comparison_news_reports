import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob_de import TextBlobDE
from nltk.tokenize import word_tokenize
import spacy
from PyMultiDictionary import MultiDictionary
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

input_file_name = "input_text.txt"
input_file_name2 = "input_text2.txt"

full_text = ""
full_text2 = ""

with open(input_file_name, 'r') as input_file:
    for line in input_file:
        full_text += line  

with open(input_file_name2, 'r') as input_file:
    for line in input_file:
        full_text2 += line 
    
word_list = word_tokenize(full_text)
word_list2 = word_tokenize(full_text2)

frequency = Counter(word_list)
frequency_of_frequency = Counter(frequency.values())

word_list = set(word_list)
word_list2 = set(word_list2)
print(len(word_list))

def find_diffrent_words(word_list,word_list2):
    word_list.difference_update(word_list2)
 
    return word_list
   
wordlist_diffrent = find_diffrent_words(word_list,word_list2)
print(len(wordlist_diffrent))
print(find_diffrent_words(word_list,word_list2))
