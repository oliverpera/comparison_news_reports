import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob_de import TextBlobDE
from nltk.tokenize import word_tokenize
import spacy
from PyMultiDictionary import MultiDictionary
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter




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
    


word_list = word_tokenize(full_text)
word_list2 = word_tokenize(full_text2)

häufigkeit = Counter(word_list)
häufigkeit_der_häufigkeiten = Counter(häufigkeit.values())









word_list = set(word_list)
word_list2 = set(word_list2)
print(len(word_list))




def find_diffrent_words(word_list,word_list2):
    word_list.difference_update(word_list2)
 
    return word_list
   



wordlist_diffrent = find_diffrent_words(word_list,word_list2)

print(len(wordlist_diffrent))


print(find_diffrent_words(word_list,word_list2))


text = "Merkel sicherte betroffenen Unternehmen umfassende Unterstützung zu. Für die Wirtschaft, für große Unternehmen, Geschäfte, Restaurants oder Freiberufler . Und die nächsten Wochen würden noch schwerer. „Ich versichere Ihnen: Die Bundesregierung tut alles, was sie kann, um die wirtschaftlichen Auswirkungen abzufedern – und vor allem um Arbeitsplätze zu bewahren.“ Die Regierung könne und werde „alles einsetzen, was es braucht, um unseren Unternehmern und Arbeitnehmern durch diese schwere Prüfung zu helfen“. Merkel ging auch auf  ein, die in vielen Supermärkten für leere Regale sorgten. Alle könnten sich darauf verlassen, dass die die Lebensmittelversorgung jederzeit gesichert sei. Wenn Regale einen Tag mal leer geräumt seien, würden sie nachgefüllt. „Vorratshaltung ist sinnvoll, war es im Übrigen immer schon“, betonte Merkel. „Aber mit Maß; hamstern, als werde es nie wieder etwas geben, ist sinnlos und letztlich vollkommen unsolidarisch.“ Nach Einschätzung von Experten könnte die Corona-Epidemie rasch voranschreiten. Das Robert-Koch-Institut warnte vor bis zu zehn Millionen Infizierten bis Juni, sollten sich die Menschen nicht an Abstands- und Hygienevorgaben halten. Laut RKI gibt es im Moment ein exponentielles Wachstum. Die Epidemie werde noch viele Wochen und Monate unterwegs sein. Derzeit seien mehr als 10.000 Menschen infiziert."

ananlysis = TextBlobDE(text)
print(ananlysis.sentiment)


