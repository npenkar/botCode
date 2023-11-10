import ccxt
import config
import json
import time
import random

bnbapi = ccxt.binance()
bnsapi = ccxt.bitbns()
bnsapi.apiKey = config.apiKey
bnsapi.secret = config.secret
# print(bnsapi.requiredCredentials) 
# print(bnsapi.checkRequiredCredentials())

print(bnsapi.fetch_markets)