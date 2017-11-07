import re
from funcs.config import Clothing, Parameters
from funcs.bot import Find

parse_string = '/shop/jackets/koknvfmbr/g91sqo5dv'

options = ['shirts','acket','accessories']

# for option in options:
#     if re.search( option, parse_string, re.M|re.I):
#         print('Matched: ' + option)
#     else:
#         print('No match')
#
# for item in Clothing.clothing_types.items():
#     print(item[1]['parse'])

print("lets see if this works")
goodluck = Find(Clothing, Parameters)
print(goodluck.searches)
