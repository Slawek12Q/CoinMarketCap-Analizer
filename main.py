import requests

res = requests.get('https://coinmarketcap.com/')
print(type(res))

res.status_code == requests.codes.ok
print( len(res.text))
print(res.text)