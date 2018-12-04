import smtplib


smtpObj = smtplib.SMTP_SSL('poczta.interia.pl', 465)
#send hello to our server
smtpObj.ehlo()
#encrypt the connection
#smtpObj.starttls()  -- disable because my connection is already encrypt
email = input("podaj swoj email")
password = input("podaj swoje hasło")
smtpObj.login(email, password)
header = 'Subject:Test \n'

msg = header + '\n this is test msg from mkyong.com \n\n'

smtpObj.sendmail(email, 'slawek.guzik1@gmail.com','Subject: Tak dlugo...\n'+'\nDroga Alicjo, czesc, i dzieki za ryby.Pozdrawiam, Bob')
{}

smtpObj.quit()