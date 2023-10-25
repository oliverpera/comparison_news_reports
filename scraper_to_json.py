import requests
import json
import os
from bs4 import BeautifulSoup

def create_json(headline_text, article_text, time_text):
    data = []

    if os.path.exists('article_text.json') and os.path.getsize('article_text.json') > 0:
        with open('article_text.json', 'r') as file:
            data = json.load(file)

    data.append({
        "headline": headline_text,
        "article_text": article_text,
        "date": time_text
    })

    with open('article_text.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    
with open('website_urls.txt', 'r') as source_file:
    
    with open('article_text.json', 'w', newline='', encoding='utf-8') as csvfile:
        
        for url in source_file:
                
            url_to_scrape = url.strip()

            response = requests.get(url_to_scrape)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                    
                h_elements = soup.find_all('h2')
                p_elements = soup.find_all('p')
                time_elements = soup.find_all('time')
                headline_text = ''
                article_text = ''
                time_text = ''
                    
                    
                for h_element in h_elements:
                    headline_text = headline_text + h_element.get_text().strip()

                for p_element in p_elements:
                    article_text = article_text + '\n\n' + p_element.get_text().strip()
                        
                for time_element in time_elements:
                    time_text = time_text + '\n\n' + time_element.get_text()
                        
                        
                headline_text = headline_text.replace('\n\n', '\n')
                article_text = article_text.replace('\n\n', '\n')
                time_text = time_text.replace('\n\n', '\n')
                    
                create_json(headline_text, article_text, time_text)
                    
            else:
                print("Fehler beim Abrufen der Webseite. Statuscode:", response.status_code)



