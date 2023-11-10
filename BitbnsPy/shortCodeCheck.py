import json
import config
from bitbnspy import bitbns
from urllib import response
from urllib.request import urlopen
import requests
import ssl
from urllib.request import Request, urlopen
import math

into = 3 
a = 1/100
# b = (1/ a)

print(a)

# print( truncate(12.3456, 2))
# print(math.trunc(12345.345435345 , 3))

# key = config.apiKey
# secretKey = config.secret
# bitbnsObj = bitbns(key, secretKey)

# response = bitbnsObj.getApiUsageStatus()
# print(response)


# getBalances = bitbnsObj.currentCoinBalance( 'INR')
# getBalances = bitbnsObj.currentCoinBalance( 'MATIC')
# print("Balances ===>", getBalances)
# data_json_dump = json.dumps(getBalances)
# data_json_load = json.loads(data_json_dump)
# print("data_json_load ==> ",data_json_load)

# matic_free_bal = float(data_json_load['data']['availableorderMATIC']) 
# print("matic_free_bal ==> ",matic_free_bal)
# inorderMATIC = float(data_json_load['data']['inorderMATIC']) 
# print("inorderMATIC ==> ",inorderMATIC)

# bal = float(getBalances[])
# print('Balance', bal)















# url = "https://public.coindcx.com/market_data/trade_history?pair=I-MATIC_INR&limit=1"

# ssl._create_default_https_context = ssl._create_unverified_context

# f = requests.get(url)
# print(f.text)

# response = urlopen(url)
# data_json = json.loads(response.read())
# data_json = json.loads(f.read())
# Price = float(data_json.get('p'))
# print(type(Price))
# print('price ===> ',Price)


# import urllib library


# import json

# store the URL in url as
# parameter for urlopen
# url = "https://public.coindcx.com/market_data/trade_history?pair=I-MATIC_INR&limit=1"
# ssl._create_default_https_context = ssl._create_unverified_context

# store the response of URL
# response = urlopen(url)

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# reg_url = "https:XXXXOOOO"
# req = requests.Request(url=url, headers=headers) 
# html = urlopen(req).read()

# storing the JSON response
# from url in data
# data_json = json.loads(response.read())

# print the json response
# print(html)






# req = Request(
#     url = "https://public.coindcx.com/market_data/trade_history?pair=I-MATIC_INR&limit=1",
#     headers={'User-Agent': 'Mozilla/5.0'}
# )
# webpage = urlopen(req).read()
# print(webpage)

# data_json = json.loads(webpage)
# print("data_json ==> ",data_json)
# price = float(data_json[0]['p'])



# req = Request(
#     url = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT",
#     headers={'User-Agent': 'Mozilla/5.0'}
# )
# webpage = urlopen(req).read()
# print(webpage)

# data_json = json.loads(webpage)
# print("data_json ==> ",data_json)
# price = float(data_json['price'])


# print('price ===> ',price)


# priceupdiffSell = float(price + ((price * 33)/100))
# priceupdiffSell = round(priceupdiffSell,3 )
# print("priceupdiffSell == >", priceupdiffSell)
# pricedowndiffBuy = round(float(price - ((price * 3)/100),3))
# price("pricedowndiffBuy == >", pricedowndiffBuy)
