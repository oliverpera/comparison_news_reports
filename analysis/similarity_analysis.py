from textblob_de import TextBlobDE as TextBlob

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
   



