from .config import Colors, Exchange, Parameters
import bs4 as bs
import lxml
import urllib.request
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

class Find():

    def __init__(self, clothing, parameters, sort_keywords=True, terminal_display=True):
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

                            #Sort array by priority and keywords
                            if sort_keywords:
                                self.first_sort = sorted(self.searches, key= lambda x: x['Keywords'], reverse=True)
                                self.searches = sorted(self.first_sort, key= lambda x: x['Priority'])

    def buy(self, budget=Parameters.budget, driver=Parameters.driver_location):
        cart_amount = 0

        #Iterate through URLs from self.searches
        page = webdriver.Chrome(driver)
        for item in self.searches:
            #Check if cart amount exceeds 90% of the budget
            print('Buying ' + item['Name'])
            if cart_amount > budget - (budget * .1):
                print('breaking loop')
                print(cart_amount)
                break
            #Check if item exceeds budget with existing cart
            if cart_amount + item['Price'] > budget:
                print('Too expensive')
                print(cart_amount)
                continue
            #Add item to cart
            else:
                page.get(Parameters.base_url + item['URL'])
                # buttom = page.find_element_by_class_name('button sold-out'):
                try:
                    button = page.find_element_by_xpath("//input[@value='add to cart']")
                    button.click()
                    print('IN CART')
                    cart_amount += item['Price']
                except:
                    print('Cannot buy same style twice')
                    print(cart_amount)
                    continue
        #Run checkout procedure
        #Add condition in case sold out even occurs
        page.get(Parameters.checkout_url)
        #Full name
        name = page.find_element_by_xpath("//input[@placeholder='name']")
        name.send_keys(Parameters.checkout_info['name'])
        #Email address
        email = page.find_element_by_xpath("//input[@placeholder='email']")
        email.send_keys(Parameters.checkout_info['email'])
        #Telephone number
        tel = page.find_element_by_xpath("//input[@placeholder='tel']")
        tel.send_keys(Parameters.checkout_info['tel'])
        #Shipping address
        address = page.find_element_by_xpath("//input[@placeholder='address']")
        address.send_keys(Parameters.checkout_info['address'])
        #Shipping address apartment
        apt = page.find_element_by_xpath("//input[@placeholder='apt, unit, etc']")
        apt.send_keys(Parameters.checkout_info['apt'])
        #Shipping zip code
        zipcode = page.find_element_by_xpath("//input[@placeholder='zip']")
        zipcode.send_keys(Parameters.checkout_info['zip'])
        #Shipping city
        city = page.find_element_by_xpath("//input[@placeholder='city']")
        city.send_keys(Parameters.checkout_info['city'])
        #Shipping state
        state = page.find_element_by_xpath("//select[@id='order_billing_state']/option[text()='{}']".format(Parameters.checkout_info['state']))
        state.click()
        #Shipping country
        country = page.find_element_by_xpath("//select[@id='order_billing_country']/option[text()='{}']".format(Parameters.checkout_info['country']))
        country.click()
        #Credit card number
        number = page.find_element_by_xpath("//input[@placeholder='number']")
        number.send_keys(Parameters.checkout_info['cc_number'])
        #Credit card expiration month
        month = page.find_element_by_xpath("//select[@id='credit_card_month']/option[text()='{}']".format(Parameters.checkout_info['cc_month']))
        month.click()
        #Credit card expiration year
        year = page.find_element_by_xpath("//select[@id='credit_card_year']/option[text()='{}']".format(Parameters.checkout_info['cc_year']))
        year.click()
        #Credit card CVV
        cvv = page.find_element_by_xpath("//input[@placeholder='CVV']")
        cvv.send_keys(Parameters.checkout_info['cc_cvv'])
        time.sleep(2000)
        print('Close window')
