import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/' #defining the URL of the website we want to scrape.

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if quotes:
        print("Quotes from quotes.toscrape.com:")
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]

            print(f'{text}')
            print(f'-> {author}')
            print(f'Tags: {", ".join(tags)}')
            print()
    else:
        print("No quotes found.")
else:
    print('Failed to retrieve data from quotes.toscrape.com.')
