from bitbnspy import bitbns
from operator import itemgetter

b = bitbns.publicEndpoints()

ticker = b.fetchTickers()
# print(ticker)
# print("=====******=====******=====******=====")
insideData = ticker['data']
# print('insideData: ===>>>',insideData)

eachCoins = insideData.keys()
# print("eachCoin ==> ", eachCoins)

# ==> getOnly INR pairs(exclude USDT)
# for eachCoins in insideData.keys():
#     if 'USDT' not in eachCoins:
#         print(eachCoins)

filteredINRPairs = []
for pairs, pairData in insideData.items():
    if 'USDT' not in pairs:
        # print(pairs, pairData)
        # print(pairs)
        if 'last_traded_price' in pairData:
            lastPrice = pairData.get('last_traded_price')
        else:
            lastPrice = 0
        # print("lastPrice==>", lp)
        if 'volume' in pairData['volume'] is not None:
            volume = pairData['volume'].get('volume')
        else:
            volume = 0
        # print("volume==>", volume)
        volumeInr = round(volume * lastPrice,2)
        # print("volumeInr ==> ", volumeInr)
        BuyPrice = pairData.get('highest_buy_bid')
        # print("highest_buy_bid==>" ,BuyPrice)
        SellPrice = pairData.get('lowest_sell_bid')
        # print("lowest_sell_ask==>", SellPrice)
        Spread = round( (((SellPrice - BuyPrice)/BuyPrice)*100), 2)
        # print("Spread ==>> ",Spread)
        # print("=====><====")
        if 10 <= Spread <= 50:
            if 10000 <= volumeInr:
                if 3<= lastPrice:
                    filteredINRPairs.append({'Pairs': pairs, 'Spread' : Spread, 'volumeInr' : volumeInr})
                    # 'lastPrice': lastPrice, 'volume': volume, 'BuyPrice' : BuyPrice, 'SellPrice' : SellPrice
# print("filteredINRPairs==> ",filteredINRPairs[0])

print("=====******=====******=====******=====******=====******=====")
newSorted = []
newlist = sorted(filteredINRPairs, key=itemgetter('Spread'), reverse=True)
newSorted.append(newlist)
for elem in newlist:
        print(elem)
print("=====******=====******=====******=====******=====******=====")
for elem in newSorted:
    onePair = elem[0].get('Pairs')
    print(onePair)


AllTradeHistory = []

# tradeHistory = b.fetchTrades('BTC', 'INR', limit = 5)
# insideTH = tradeHistory['data']
# print("===> insideTH:", insideTH)

# allkeys = insideTH.items()
# print(allkeys)


# for timestamp, type in insideTH.key():
#     print(timestamp, type)
#     timestamp = insideTH.get('timestamp')
#     print(" timestamp===> ", timestamp)
    