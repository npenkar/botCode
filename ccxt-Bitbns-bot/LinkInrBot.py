import ccxt
import config
import json
import time
import random

bnbapi = ccxt.binance()
bnsapi = ccxt.bitbns()
bnsapi.apiKey = config.apiKey
bnsapi.secret = config.secret

bnsticker = bnsapi.fetch_ticker('LINK/INR')
# print(bnsticker)

GetAllOpenOrders = bnsapi.fetch_open_orders(symbol='LINK/INR', limit=None, params={})
dumpOpenOrder = json.dumps(GetAllOpenOrders)
loadOpenOrder = json.loads(dumpOpenOrder) 
openOrdersCount = len(loadOpenOrder)
print('All Open orders count===>', openOrdersCount)
# loop2 start
print('All Open orders ===>', GetAllOpenOrders)