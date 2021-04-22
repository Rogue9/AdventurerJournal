import requests
from bs4 import BeautifulSoup
import lxml

class Realtor:
    def __init__(self):
        self.len = ""
        self.address = ""
        self.link = ""
        self.formatted_listings = {}
        self.accept_language = "en-US,en;q=0.9"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"

    def get_listings(self, url):
        response = requests.get(url, headers={"User-Agent":self.user_agent, "Accept-Language":self.accept_language})
        zillow_site = response.text
        soup = BeautifulSoup(zillow_site, 'html.parser')
        prices= soup.find_all(class_="list-card-price")
        links = soup.find_all(class_="list-card-link", name='a')
        list_links = [a['href'] for a in soup.find_all(class_="list-card-link", name='a', tabindex='0')]
        for index in range(len(list_links)):
            if not list_links[index].startswith('http'):
                list_links[index] = 'https://www.zillow.com' + list_links[index]
        addresses = soup.find_all(class_="list-card-addr")
        self.listing_number = len(prices)
        self.format_listings(prices=prices, links=list_links, addresses=addresses)


    def format_listings(self, prices, links, addresses):
        for i in range(len(prices)):
            self.formatted_listings[i] = [addresses[i].getText(), prices[i].getText(), links[i]]


