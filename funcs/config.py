class Parameters():
    parse_url = 'http://www.supremenewyork.com/shop/all'
    base_url = 'http://www.supremenewyork.com'
    cart_url = 'http://www.supremenewyork.com/shop/cart'
    checkout_url = 'https://www.supremenewyork.com/checkout'
    budget = 500

class Clothing():
    clothing_types = {'Accessories': {'url': 'accessories', \
                        'parse': True, \
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
                        'parse': True, \
                        'priority': 2, \
                        'keywords': None}, \
                      'Pants': {'url': 'pants',
                        'parse': True, \
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
    global_keywords = ['woodbine']
    exclude_keywords = ['hanes']

class Exchange():

    JPY_USD = .0088

    def USD_JPY(self,amount):
        return amount * JPY_USD

class Colors():
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'
