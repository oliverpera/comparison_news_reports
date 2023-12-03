import spacy
from textblob_de import TextBlobDE
import random
from difflib import SequenceMatcher

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def split_into_entries(text_content, par):
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text_content)
    
    counter = 0
    to_add = ''
    
    sentences = [sent.text for sent in doc.sents]
    processed_sentences = [sentence.replace('\n', '') for sentence in sentences]
    splitted_list = []
    
    for sentence in processed_sentences:
        counter += 1
        if counter <= par:
            to_add += sentence + ' '
        else:
            splitted_list.append(to_add)
            to_add = ''
            counter = 0
                
    return splitted_list

def analysis(list_text):
    values = {}
    
    analyse = TextBlobDE(list_text)
    print(analyse.sentiment.subjectivity)
    
    for text in list_text:
        analyse = TextBlobDE(text)
        
        if analyse.sentiment.subjectivity > 0.05:
            if not text in values:
                values[text] = analyse.sentiment.subjectivity
            
    return values

def analyze_text(text_content, values):
    analyse = TextBlobDE(text_content)
    
    if analyse.sentiment.subjectivity > 0.17:
        values[text_content] = analyse.sentiment.subjectivity
        
    return values   

def process_text(text_content):
    values = {}

    for x in range(1, 11, 1):        
        print("\n Iteration :", x, " / Identified: ", len(values))
        
        list_to_check = split_into_entries(text_content, x)
        
        for text in list_to_check:
            analyze_text(text, values)
            
    return values
        
def print_dict(values):
    if len(values) > 0:
        print("Counter: ", len(values))
        
        for key, value in values.items():
            print(f"\nKey: {key}, Value: {value}\n\n")
    else:
        print("Counter: ", len(values))
        
def get_min_max_values(dict_p):
    if len(dict_p) == 0:
        return None, None
    
    values = list(dict_p.values())
    min_value = min(values)
    max_value = max(values)
    return min_value, max_value
    
        
def compare_and_delete(d):
    keys_to_delete = []

    for key1 in d:
        for key2 in d:
            if key1 != key2 and key1 not in keys_to_delete and key2 not in keys_to_delete:
                
                similarity = SequenceMatcher(None, key1, key2).ratio()
                
                if similarity > 0.5:
                    if d[key1] < d[key2]:
                        keys_to_delete.append(key1)
                        
                    elif d[key1] == d[key2]:
                        if len(key1) < len(key2):
                            keys_to_delete.append(key1)
                            
                    else:
                        keys_to_delete.append(key2)

    for key in keys_to_delete:
        del d[key]

    return d
        
def main():
    file_path = 'input_text.txt' 

    text_content = read_text_file(file_path)
        
    values = process_text(text_content)
    
    print_dict(values)
    low, high = get_min_max_values(values)
    print(f"Dictionary: Min: {low}, Max: {high}")
    
    cleaned_values = compare_and_delete(values)
    print_dict(cleaned_values)
    cleaned_low, cleaned_high = get_min_max_values(values)
    print(f"Cleaned Dictionary: Min: {cleaned_low}, Max: {cleaned_high}")

if __name__ == "__main__":
    main()

