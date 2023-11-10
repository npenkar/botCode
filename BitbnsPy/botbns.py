import json

from bitbnspy import bitbns

# from bitbnspy import bitbns

import config
key = config.apiKey
secretKey = config.secret
bitbnsObj = bitbns(key, secretKey)
# print('APIstatus: =',  bitbnsObj.getApiUsageStatus)

# getPairTicker = bitbnsObj.getTickerApi('DOGE') 
# print(' PairTicker : ', getPairTicker)
print('====================================')
# dumpBid = json.dumps(getPairTicker)
# loadBid = json.loads(dumpBid)
# getBid = loadBid['highest_buy_bid']
# print('highest buy: ', loadBid)
print('====================================')
# OpenOrders = bitbnsObj.listOpenOrders('DOGE')
# print(OpenOrders)

bitbnsObj = bitbns.publicEndpoints()
getTickers = bitbnsObj.fetchTickers()
dumpTickers = json.dumps(getTickers)
loadTickers = json.loads(dumpTickers)
print(loadTickers)


