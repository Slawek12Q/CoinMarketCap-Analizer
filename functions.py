import time
import smtplib
import requests
import bs4
from url import URLs


listOfUrls = set(URLs)

myDataFile = open('C:\\Users\\Lenovo\\Desktop\\myData.txt')

myEmail = myDataFile.readline().strip()
myPassword = myDataFile.readline().strip()
subscriberEmail = myDataFile.readline().strip()
changePrice = int(myDataFile.readline().strip())

def check_the_market():
    message = """Subject:Attention It's time to sell or buy  \n"""
    someChages = False

    while True:

        for i in listOfUrls:

            res = requests.get(i.value)
            different = 0
            beautifulSoapElement = bs4.BeautifulSoup(res.text, features="html.parser")

            changes = beautifulSoapElement.select(
                'html > body > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div > span:nth-of-type(2)')

            different = changes[0].getText()[2:len(changes[0].getText()) - 4]
            different = float(different)
            print(i.name, different)

            if -changePrice >= different or different >= changePrice:
                someChages = True
                message += f"""\nYour coin which you posses: {i.name}
                               #             change yourself price about: {different}% \n\n"""

        print("\n\n\n")

        if someChages:
            return message

        time.sleep(60)


def send_email(message):
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(myEmail, myPassword)
    smtpObj.sendmail(myEmail, subscriberEmail, message)
    {}
    smtpObj.close()