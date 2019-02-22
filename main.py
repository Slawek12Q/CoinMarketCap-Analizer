import time
import smtplib
import requests
import bs4
from enum import Enum

class URLs(Enum):
    BITCOIN = "https://coinmarketcap.com/currencies/bitcoin/"
    RIPPLE = "https://coinmarketcap.com/currencies/ripple/"
    LITECOIN = "https://coinmarketcap.com/currencies/litecoin/"
    LISK = "https://coinmarketcap.com/currencies/lisk/"
    DOGECOIN = "https://coinmarketcap.com/currencies/dogecoin/"
    TRON = "https://coinmarketcap.com/currencies/tron/"
    STEEM = "https://coinmarketcap.com/currencies/steem/"
    ETHEREUM="https://coinmarketcap.com/currencies/ethereum/"

listOfUrls = set(URLs)

myDataFile = open('C:\\Users\\Lenovo\\Desktop\\myData.txt')

myEmail = myDataFile.readline().strip()
myPassword = myDataFile.readline().strip()
subscriberEmail = myDataFile.readline().strip()

message = """Subject:Attention It's time to sell or buy  \n"""

startTime = time.time()

someChages = False


while True:

    for i in listOfUrls:

        res = requests.get(i.value)
        different = 0
        beautifulSoapElement = bs4.BeautifulSoup(res.text, features="html5lib")

        changes = beautifulSoapElement.select('html > body > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div > span:nth-of-type(2)')

        different = changes[0].getText()[2:len(changes[0].getText())-4]
        different = float(different)
        print(i.name, different)


        if -5 >= different or different >= 2:

            someChages = True
            message += f"""\nYour coin which you posses: {i.name}
                           #             change yourself price about: {different}% \n\n"""

    print("\n\n\n")


    if someChages:
        break

    time.sleep(60)

smtpObj = smtplib.SMTP_SSL('poczta.interia.pl', 465)

# send hello to our server
smtpObj.ehlo()
# encrypt the connection
#smtpObj.starttls()  #-- disable because my connection is already encrypt

smtpObj.login(myEmail, myPassword)

smtpObj.sendmail(myEmail, subscriberEmail, message)
{}

smtpObj.quit()





stopTime = time.time()

print(stopTime - startTime)

