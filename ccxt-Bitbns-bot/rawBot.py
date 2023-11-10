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

while True:
    GetAllOpenOrders = bnsapi.fetch_open_orders(symbol=config.pair, limit=None, params={})
    dumpOpenOrder = json.dumps(GetAllOpenOrders)
    loadOpenOrder = json.loads(dumpOpenOrder) 
    openOrdersCount = len(loadOpenOrder)
    print('All Open orders count===>', openOrdersCount)
    # loop2 start
    i = 0
    while i<openOrdersCount:
        getOpenOrderData = (loadOpenOrder[i])
        orderid = getOpenOrderData.get('id')
        cancelOpenOrder = bnsapi.cancel_order(id= orderid, symbol=config.pair)
        print(cancelOpenOrder)
        i=i+1  
    # loop2 end
    
    placedelay = random.randint(1,3)
    print('place order delay: ',placedelay)
    time.sleep(placedelay)
    
    bnbticker = bnbapi.fetch_ticker(config.pair)
    # print(bnbticker)
    bnblastPrice = bnbticker['close']
    print(config.pair,'Binance last price: ', bnblastPrice)
    print('====================================')
    
    bnsticker = bnsapi.fetch_ticker(config.pair)
    # print(config.pair,'bnsticker: ',bnsticker)
    # print('====================================')
       
    bnslastPrice = bnsticker['close']
    print(config.pair,'Bitbns last price: ', bnslastPrice)  
     
    print('====================================')
    getBnsBid = bnsticker['bid']
    print('highest buy: ', getBnsBid)

    getBnsAsk = bnsticker['ask']
    print('lowest sell: ', getBnsAsk)
    print('====================================')

    updatedBuyPrice = getBnsBid + 0.0000002
    print('updatedBuyPrice: ',updatedBuyPrice)
    updatedSellPrice = getBnsAsk - 0.0000002
    print('updatedSellPrice:',updatedSellPrice)
    print('====================================')

    # extra calculation
    discountedBuyRate = bnblastPrice - bnblastPrice* (15/100)
    print('discountedBuyRate: ',discountedBuyRate)

    discountedSellRate = bnblastPrice + bnblastPrice* (5/100)
    print('discountedSellRate: ',discountedSellRate)

    # compare best rates
    if (discountedBuyRate < updatedBuyPrice ):
        bestBuyRate = discountedBuyRate
    else:
        bestBuyRate = updatedBuyPrice
        
    print('bestBuyRate: ',bestBuyRate)

    if (discountedSellRate > updatedSellPrice ):
        bestSellRate = discountedSellRate
    else:
        bestSellRate = updatedSellPrice
        
    print('bestSellRate: ',bestSellRate)
    print('====================================') 
    # getBalances
    getBalances = bnsapi.fetch_free_balance()
    # print(balances) /get all balances
    dumpBalances = json.dumps(getBalances)
    loadBalances = json.loads(dumpBalances)
    getDOGEBalances= loadBalances[config.first_currency]
    getUSDTBalances= loadBalances[config.second_currency]
    print('DOGE: ',getDOGEBalances)
    print('USDT: ',getUSDTBalances)
    print('====================================') 

    if (getDOGEBalances < 1):
        print('No balance to place Sell order')
    else:
        temp_sell_order_amount = int(getDOGEBalances - (getDOGEBalances * (20/100)))
        print('temp_sell_order_amount: ',temp_sell_order_amount)
        sellOrderAmount = int(random.randint(temp_sell_order_amount,getDOGEBalances))
        # sellOrderAmount = int(getDOGEBalances)    #100% sell
        print('sellOrderAmount: ',sellOrderAmount)
        placeLimitSellOrder = bnsapi.create_limit_sell_order(config.pair, sellOrderAmount, bestSellRate)
        print(placeLimitSellOrder)
        
    print('====================================')     
        
    buyOrderFees = getUSDTBalances* (0.25/100)
    print('buyOrderFees :',buyOrderFees)
    calculated_buy_order_amount = int((getUSDTBalances - buyOrderFees)/updatedBuyPrice)
    print('calculated_buy_order_amount:',calculated_buy_order_amount)
    temp_buy_order_amount = int(calculated_buy_order_amount - (calculated_buy_order_amount * (20/100)))
    print('temp_buy_order_amount:',temp_buy_order_amount)
        
    if (getUSDTBalances < 1):
        print('No balance to place Buy order')
    else:
        buyOrderAmount = int(random.randint(temp_buy_order_amount,calculated_buy_order_amount))
        # buyOrderAmount = int(calculated_buy_order_amount) #100% buy
        print('buyOrderAmount: ',buyOrderAmount)
        placeLimitBuyOrder = bnsapi.create_limit_buy_order(config.pair,buyOrderAmount,bestBuyRate)
        print(placeLimitBuyOrder) 
    
    print('=*=*=*=*=*==*=*=*=*=*==*=*=*=*=*==*=*=*=*=*=*=*==*=*=*=*=*=')
    canceldelay = random.randint(20,50)
    print('cancel order delay: ',canceldelay)
    time.sleep(canceldelay)
    print('====================================')  
