import spacy
from textblob_de import TextBlobDE
import random
from queue import Queue


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def split_into_entries(text, par):
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)
    
    counter = 0
    to_add = ''
    
    sentences = [sent.text for sent in doc.sents]
    cleaned_sentences = [sentence.replace('\n', '') for sentence in sentences]
    aggregated_list = []
    
    for sentence in cleaned_sentences:
        counter += 1
        if counter <= par:
            to_add += sentence + ' '
        else:
            aggregated_list.append(to_add)
            to_add = ''
            counter = 0
                
    return aggregated_list

def analysis(list_text):
    values = []
    
    for text in list_text:
        analyse = TextBlobDE(text)
        
        if analyse.sentiment.subjectivity > 0.05:
            values.append(analyse.sentiment.subjectivity)
            
    return values

def analysis_random(text_content):
    values = {}
    
    for i in range(10):
        random_number = random.randint(3, 15)
        list_to_check = split_into_entries(text_content, random_number)

        for text in list_to_check:
            analyse = TextBlobDE(text)
            if analyse.sentiment.subjectivity > 0.05:
                if not text in values:
                    values[text] = analyse.sentiment.subjectivity

    return values

def create_queue(text_content):
    lifo_queue = Queue()

    for i in range(3, 15, 1):
        text_to_check = split_into_entries(text_content, i)
        
        for sentence in text_to_check:
            lifo_queue.put(sentence)
         
        size = lifo_queue.qsize()
        
        if not lifo_queue.empty():
            lifo_queue.put(None)
        
        
        element1 = lifo_queue.get()
        element2 = lifo_queue.get()
        element3 = lifo_queue.get()
        
        print("Entferntes Element 1:", element1)
        print("Entferntes Element 2:", element2)
        print("Entferntes Element 3:", element3)


def main():
    file_path = 'second_text.txt' 

    text_content = read_text_file(file_path)
    entries_spacy = split_into_entries(text_content, 8)
        
   # print(analysis(entries_spacy))
   # print(analysis_random(text_content))
    
    create_queue(entries_spacy)


if __name__ == "__main__":
    main()

