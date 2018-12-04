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



listOfUrls = set(URLs)

myEmail = input("enter your email: ")
password = input("enter your password: ")
subscriberEmail = input("enter subscriber email: ")
message = """Subject:Attention It's time to sell or buy  \n"""

startTime = time.time()

for a in range(1):

    for i in listOfUrls:

        res = requests.get(i.value)
        different = 0
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



        if -5 >= different or different >= 5:
            smtpObj = smtplib.SMTP_SSL('poczta.interia.pl', 465 )
            #send hello to our server
            smtpObj.ehlo()
            #encrypt the connection
            #smtpObj.starttls()  -- disable because my connection is already encrypt

            message += f"""\nYour criptocurent which you posses: {i.name}
                        change your valuable abut: {different}% """

            smtpObj.login(myEmail, password)

            smtpObj.sendmail(myEmail, subscriberEmail,message)

            {}

            smtpObj.quit()


stopTime = time.time()

print(stopTime - startTime)

