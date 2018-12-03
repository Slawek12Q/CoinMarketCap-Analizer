import time

import requests
import bs4
from enum import Enum

class URLs(Enum):
    BITCOIN = "https://coinmarketcap.com/currencies/bitcoin/"
    RIPPLE = "https://coinmarketcap.com/currencies/ripple/"
    LITECOIN = "https://coinmarketcap.com/currencies/litecoin/"
    LISK = "https://coinmarketcap.com/currencies/lisk/"
    DOGECOIN = "https://coinmarketcap.com/currencies/dogecoin/"



listOfUrls = set(URLs)

startTime = time.time()

for a in range(5):

    for i in listOfUrls:

        res = requests.get(i.value)

        beautifulSoapElement = bs4.BeautifulSoup(res.text, features="html5lib")

        element_negative = beautifulSoapElement.select('.negative_change')
        element_positive = beautifulSoapElement.select('.positive_change')

        if len(element_negative) > 0:
            different = element_negative[0].getText()[2:len(element_negative[0].getText())-3]
            different = float(different)
            print(i.name, different)

        else:
            different = element_positive[0].getText()[2:len(element_positive[0].getText())-3]
            different = float(different)
            print(i.name, different)



stopTime = time.time()

print(stopTime - startTime)