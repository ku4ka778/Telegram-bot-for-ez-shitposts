import requests
from bs4 import BeautifulSoup
import time
import random



class Jokes:

    def __init__(self, count):
        self.count = count
        self.url = ' http://shortiki.com/export/api.php?format=xml&type=random&amount=' + self.count
        print(self.url)

    async def filtering(self):
        # Getting jokes
        self.res = requests.get(self.url)
        self.soup = BeautifulSoup(self.res.text, features='xml')
        i = 0
        self.joke = ''
        # Filtering the received XML
        item = self.soup.find_all('item')
        for item in item:
            self.title = item.find('title')
            self.desc = item.find('description')
            self.joke = self.joke + str(i+1) + '. ' + self.title.text + ':\n' + self.desc.text + '\n'
            i +=1
        time.sleep(random.randint(1, 5))
        return self.joke
