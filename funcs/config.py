class Parameters():
    parse_url = 'http://www.supremenewyork.com/shop/all'
    base_url = 'http://www.supremenewyork.com'
    cart_url = 'http://www.supremenewyork.com/shop/cart'
    checkout_url = 'https://www.supremenewyork.com/checkout'

class Clothing():
    clothing_types = {'Accessories': {'url': 'accessories', \
                        'parse': True, \
                        'priority': 7, \
                        'keywords': ['woodbine','akira','tee','tag']}, \
                      'Bags': {'url': 'bags', \
                        'parse': False, \
                        'priority': 5, \
                        'keywords': None}, \
                      'Hats': {'url': 'hats', \
                        'parse': False, \
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
                        'parse': False, \
                        'priority': 0, \
                        'keywords': None}, \
                      'Skate': {'url': 'skate', \
                        'parse': True, \
                        'priority': 6, \
                        'keywords': None}, \
                      'Sweatshirts': {'url': 'sweatshirts', \
                        'parse': False, \
                        'priority': 3, \
                        'keywords': None}, \
                      'Tops/ Sweaters': {'url': 'tops-sweaters', \
                        'parse': True, \
                        'priority': 1, \
                        'keywords': None}}
    global_keywords = ['nike','akira','Independent','wheels','snake','thermal']

class Colors():
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'
