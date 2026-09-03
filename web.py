'''
                                            request
                                            -------
                                            -------

- request module is used sto send the HTTP request to the server


'''
from bs4 import BeautifulSoup

import requests
url = "https://books.toscrape.com/"
response = requests.get(url)
tit = BeautifulSoup(response.text, 'html.parser')
books = tit.find_all('h3')
for book in books:
    tit = book.find('a').get('title')
    print(tit)