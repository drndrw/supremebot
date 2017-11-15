from .config import Colors, Exchange
import bs4 as bs
import lxml
import urllib.request
import re
import time

class Find():

    def __init__(self, clothing, parameters, terminal_display=True):
        self.parser = urllib.request.urlopen(parameters.parse_url).read()
        self.directory = bs.BeautifulSoup(self.parser,'lxml')
        self.searches = []

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

                            #Check if sold out (on page)
                            if self.item_page.find(attrs={'class':'button sold-out'}):
                                if terminal_display:
                                    print(Colors.BOLD + self.item_page.title.text[9:] + Colors.END)
                                    print(Colors.RED + "  SOLD OUT" + Colors.END)
                                continue

                            #Search category keywords in title
                            self.keywords = 0
                            if item[1]['keywords']:
                                for keyword in item[1]['keywords']:
                                    if re.search(keyword, self.item_page.title.text, re.M|re.I):
                                        self.keywords += 1

                            #Search global keywords in title
                            #In the future, check for duplicate keywords in against category keywords, not important now
                            if clothing.global_keywords:
                                for keyword in clothing.global_keywords:
                                    if re.search(keyword, self.item_page.title.text, re.M|re.I):
                                        self.keywords += 1

                            #Locate the price
                            self.price = self.item_page.find(attrs={'data-currency':'USD'})
                            if self.price:
                                self.price = int(self.price.text[1:])
                            else:
                                #Will worry about conversions later
                                self.price = 0

                            #Find sizes
                            self.sizes_select = self.item_page.find_all('option')
                            if self.sizes_select:
                                self.sizes = [size.text for size in self.sizes_select]
                            else:
                                self.sizes = None

                            #Terminal Display
                            if terminal_display:
                                print(Colors.BOLD + self.item_page.title.text[9:] + Colors.END)
                                print("  Category: " + item[0])
                                print("  Price: " + str(self.price))
                                print("  Keywords: " + str(self.keywords))
                                print("  Sizes: " + ', '.join(self.sizes) if self.sizes else 'N/A')

                            #Write to output array
                            self.searches.append({'Category': item[0],'Name': self.item_page.title.text[9:],'Price': self.price if self.price else 0,'URL': link.a.get('href'),'Keywords': int(self.keywords), 'Sizes': self.sizes,'Priority':item[1]['priority']})

    def prioritize():
        #Iterate through dictionary (self.searches), using the priority number (in ascending order)
        for item in self.searches:
            print
        #Assign individual priority numbers to each item, starting with the highest number of keyword matches
        # for item in
        return None
