import time
from functions import check_the_market, send_email


startTime = time.time()


message = check_the_market()

send_email(message)


stopTime = time.time()

print(stopTime - startTime)

