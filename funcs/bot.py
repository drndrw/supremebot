from .config import Colors
import bs4 as bs
import lxml
import urllib.request
import re
import time

class Find():

    def __init__(self, clothing, parameters):
        self.parser = urllib.request.urlopen(parameters.parse_url).read()
        self.directory = bs.BeautifulSoup(self.parser,'lxml')
        self.searches = []
        self.old_item = self.directory.find('article')
        # while True:
        #     self.new_item = self.directory.find('article')
        #     if self.new_item == self.old_item:
        #         print('NO UPDATES: ' + str(time.time()))
        #         continue
        #     else:
        #         print('UPDATED: ' + str(time.time()))
        #         break

        for link in self.directory.find_all('article'):
            #Start loop over if item is sold out on main page
            if link.find(class_="sold_out_tag"):
                continue
            #Investigate if item is available
            else:
                #Check if item is in a category of interest
                for item in clothing.clothing_types.items():
                    #Check if category of interest is searchable
                    if item[1]['parse']:
                        #Check if category matches URL
                        if re.search(item[1]['url'], link.a.get('href'), re.M|re.I):
                            # print(parameters.base_url + link.a.get('href'))
                            self.item_parse = urllib.request.urlopen(parameters.base_url + link.a.get('href')).read()
                            self.item_page = bs.BeautifulSoup(self.item_parse,'lxml')
                            print(Colors.BOLD + self.item_page.title.text + Colors.END)
                            #Check if sold out (on page)
                            if self.item_page.find(attrs={'class':'sold-out'}):
                                print(Colors.RED + "SOLD OUT" + Colors.END)
                                continue
                            #Search category keywords in title
                            self.keywords = 0
                            if item[1]['keywords']:
                                for keyword in item[1]['keywords']:
                                    if re.search(keyword, self.item_page.title.text, re.M|re.I):
                                        self.keywords += 1
                            #Search category keywords in title
                            if clothing.global_keywords:
                                for keyword in clothing.global_keywords:
                                    if re.search(keyword, self.item_page.title.text, re.M|re.I):
                                        self.keywords += 1
                            print("Keywords: " + str(self.keywords))
                            #Locate the price, add to object
                            self.price = self.item_page.find(attrs={'data-currency':'USD'})
                            if self.price:
                                print(int(self.price.text[1:]))
                            else:
                                print('Currency not in USD.')
                            #Search tags against URL title, add number of matches to object
                            self.searches.append(link.a.get('href'))
        # return self.searches
                # available_url = urllib.request.urlopen('http://www.supremenewyork.com' + link.a.get('href')).read()
                # available = bs4.BeautifulSoup(available_url,'lxml')
                # print('\033[1m' + available.title.text[9:] + '\033[0m')
