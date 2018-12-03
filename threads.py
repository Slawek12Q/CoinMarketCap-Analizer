import time
import threading
import requests
import bs4
from enum import Enum

class URLs(Enum):
    BITCOIN = "https://coinmarketcap.com/currencies/bitcoin/"
    RIPPLE = "https://coinmarketcap.com/currencies/ripple/"
    LITECOIN = "https://coinmarketcap.com/currencies/litecoin/"
    LISK = "https://coinmarketcap.com/currencies/lisk/"
    DOGECOIN = "https://coinmarketcap.com/currencies/dogecoin/"



def checUrl (url):
    res = requests.get(url.value)

    beautifulSoapElement = bs4.BeautifulSoup(res.text, features="html5lib")

    element_negative = beautifulSoapElement.select('.negative_change')
    element_positive = beautifulSoapElement.select('.positive_change')

    if len(element_negative) > 0:
        different = element_negative[0].getText()[2:len(element_negative[0].getText()) - 3]
        different = float(different)
        print(i.name, different)

    else:
        different = element_positive[0].getText()[2:len(element_positive[0].getText()) - 3]
        different = float(different)
        print(i.name, different)


listOfUrls = set(URLs)



startTime = time.time()

for a in range(5):

    urlThreads = []

    for i in listOfUrls:

        #checUrl(i)
        print(i.name)
        urlThread = threading.Thread(target=checUrl, args=(i,))
        urlThreads.append(urlThread)
        urlThread.start()


    for urlThread in urlThreads:
        urlThread.join()




stopTime = time.time()

print(stopTime - startTime)