import re
from funcs.config import Clothing, Parameters
from funcs.bot import Find

supreme = Find(Clothing, Parameters)
print(supreme.buy())
print(supreme.searches)
