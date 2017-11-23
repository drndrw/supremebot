import os

class Parameters():

    #Shop URLs
    parse_url = 'http://www.supremenewyork.com/shop/new'
    base_url = 'http://www.supremenewyork.com'
    cart_url = 'http://www.supremenewyork.com/shop/cart'
    checkout_url = 'https://www.supremenewyork.com/checkout'
    budget = 500

    #Selenium
    driver_location = '/Users/drndrw/Downloads/chromedriver'

    #Customer information
    checkout_info = {
        'name': os.getenv('SUPREME_NAME','John Doe'), \
        'email': os.getenv('SUPREME_EMAIL','supreme@supremenyc.com'), \
        'tel': os.getenv('SUPREME_TEL','5551234567'), \
        'address': os.getenv('SUPREME_EMAIL','1234 Supreme Ct.'), \
        'apt': os.getenv('SUPREME_APT','69'), \
        'zip': os.getenv('SUPREME_ZIP','12345'), \
        'city': os.getenv('SUPREME_CITY','New York City'), \
        'state': os.getenv('SUPREME_STATE','CA'), \
        'country': os.getenv('SUPREME_COUNTRY','USA'), \
        'cc_number': os.getenv('SUPREME_CC_NUMBER','1234567890123456'), \
        'cc_month': os.getenv('SUPREME_CC_MONTH','11'), \
        'cc_year': os.getenv('SUPREME_CC_YEAR','2020'), \
        'cc_cvv': os.getenv('SUPREME_CC_CVV','123')
    }

class Clothing():
    clothing_types = {'Accessories': {'url': 'accessories', \
                        'parse': False, \
                        'priority': 7, \
                        'keywords': None}, \
                      'Bags': {'url': 'bags', \
                        'parse': True, \
                        'priority': 5, \
                        'keywords': None}, \
                      'Hats': {'url': 'hats', \
                        'parse': True, \
                        'priority': 4, \
                        'keywords': None}, \
                      'Jackets': {'url': 'jackets',
                        'parse': False, \
                        'priority': 2, \
                        'keywords': None}, \
                      'Pants': {'url': 'pants',
                        'parse': False, \
                        'priority': 8, \
                        'keywords': None}, \
                      'Shirts': {'url': 'shirts', \
                        'parse': True, \
                        'priority': 0, \
                        'keywords': None}, \
                      'Skate': {'url': 'skate', \
                        'parse': True, \
                        'priority': 6, \
                        'keywords': None}, \
                      'Sweatshirts': {'url': 'sweatshirts', \
                        'parse': True, \
                        'priority': 3, \
                        'keywords': None}, \
                      'Tops/ Sweaters': {'url': 'tops-sweaters', \
                        'parse': True, \
                        'priority': 1, \
                        'keywords': None}}
    global_keywords = ['snake','fuck','black','snake','levi']
    exclude_keywords = ['hanes']

class Exchange():

    JPY_USD = .0088

    def USD_JPY(self,amount):
        return amount * JPY_USD

class Colors():
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'
