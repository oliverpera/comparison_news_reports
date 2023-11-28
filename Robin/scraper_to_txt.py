import requests
from bs4 import BeautifulSoup

with open('website_urls.txt', 'r') as source_file:
    for line in source_file:

        url = line

        response = requests.get(url)


        if response.status_code == 200:

            html_content = response.text


            soup = BeautifulSoup(html_content, 'html.parser')


            for a in soup.findAll('a', href=True):
                a.extract()

            website_text = 'Start off Dokument'
            p_tags = soup.find_all('p')

            for p_tag in p_tags:
                website_text = website_text + '\n' + p_tag.get_text()

            website_text = website_text.replace('\n\n', '\n')
            website_text = website_text.replace('\b', '\n')
            website_text = website_text + '\n' + 'EndOffDocument' + '\n'

            with open("article_text.txt", "a", encoding='utf-8') as textdatei:

                textdatei.write(website_text)


        else:
            print(f"Fehler beim Abrufen der Website{line}. Statuscode: {response.status_code}")


