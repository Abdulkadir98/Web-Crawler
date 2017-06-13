import requests
import urllib3
from bs4 import BeautifulSoup


def web_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.bloomberg.com/quote/INDU:IND'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        price_box = soup.find('div', attrs={'class': 'price'})
        price = price_box.string
        print(price)
        # for link in soup.findAll('div', {'class':'price'}):
        #     href = link.get('href')
        #     title = link.string
        #     print(title)
        #     print(href)
        page = page + 1

web_crawler(1)


