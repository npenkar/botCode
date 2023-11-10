from distutils.command.config import config
from bitbnspy import bitbns
import json
from operator import contains, itemgetter

import config
key = config.apiKey
secretKey = config.secret
b = bitbns(key, secretKey)

b = bitbns.publicEndpoints()

ticker = b.fetchTickers()
# print(ticker)
# print("=====******=====******=====******=====")

# dumpTicker = json.dumps(ticker)
# loadTicker = json.loads(dumpTicker)
# insideData = loadTicker['data']
insideData = ticker['data']
# print('insideData: ===>>>',insideData)
# print('insideData: ===>>>',insideData['BTC']['highest_buy_bid'])
# print('insideData: ===>>>',insideData['BTC'].get('highest_buy_bid'))
# print("length of TickerAPI",len(insideData))

eachCoins = insideData.keys()
# print("eachCoin ==> ", eachCoins)


# valuess = []
# for eachCoins in insideData.keys():
#     if 'USDT' not in eachCoins:
#         print(eachCoins)

# for pairs, pairData in insideData.items():
        # print(pairs, pairData)
# pairs => BTC, ETH, BTCUSD
# pairData => data inside attr


# BTCUSDT if pairs contain("USDT")
    # skip that pair
    # else process that pair

# filteredINRPairs = []
for pairs, pairData in insideData.items():
    if 'USDT' not in pairs:
        # print(pairs, pairData)
        print(pairs)
        if 'yes_price' in pairData:
            lp = pairData.get('yes_price')
        else:
            lp = 0
        print("lastPrice==>", lp)
        if 'volume' in pairData['volume'] is not None:
            volume = pairData['volume'].get('volume')
        else:
            volume = 0
        print("volume==>", volume)
        volumeInr = volume * lp
        print("volumeInr ==> ", volumeInr)
        BuyPrice = pairData.get('highest_buy_bid')
        print("highest_buy_bid==>" ,BuyPrice)
        SellPrice = pairData.get('lowest_sell_bid')
        print("lowest_sell_ask==>", SellPrice)
        Spread = ((SellPrice - BuyPrice)/BuyPrice)*100
        print("Spread ==>> ",Spread)
        print("=====><====")
    
