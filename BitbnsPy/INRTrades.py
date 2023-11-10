import datetime
import random
import time
from bitbnspy import bitbns
import config
import json
import math
from urllib.request import urlopen
from urllib.request import Request, urlopen

def truncate(number, decimals=0):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
placedelay = random.randint(15,30)

key = config.apiKey
secretKey = config.secret
bitbnsObj = bitbns(key, secretKey)

while True:

    response = bitbnsObj.getApiUsageStatus()
    print(response)

    b = bitbns.publicEndpoints()
    ticker = b.fetchTickers()
    # print("ticker=====>",ticker)

    insideData = ticker['data']
    # print(" data=====>",insideData )
    eachCoins = insideData.keys()
    # getData = []
   
    print(' ====================>>> GET CURRENT RATES <<<====================')
    for pairs, pairData in insideData.items():
        if config.INRpair == pairs:
            last_traded_price = pairData.get('last_traded_price')
            print("last_traded_price: ", last_traded_price)
            highest_buy_bid = pairData.get('highest_buy_bid')
            print("highest_buy_bid: ", highest_buy_bid)
            lowest_sell_bid = pairData.get('lowest_sell_bid')
            print("lowest_sell_bid: ", lowest_sell_bid)

    print(' ====================>>> CALCULATE RATES <<<====================')

    avg_mid_price = truncate( ((highest_buy_bid + lowest_sell_bid)/2), config.ratePrecision)
    print("Avg Mid Price ==> ", avg_mid_price)

    orderbookSpread = truncate( (((lowest_sell_bid - highest_buy_bid)/highest_buy_bid)*100), 2)
    print("current order book Spread ===> ", orderbookSpread)
    print("bns_minimum_spread percent ===> ", config.bns_minimum_spread)
    print("obSpread midSpread percent ===> ", config.midSpread)

    up_buy_price = truncate( avg_mid_price  - (avg_mid_price *  (config.midSpread /100)), config.ratePrecision)
    print(" percent up_buy_price ==> ", up_buy_price)
    down_sell_price = truncate( avg_mid_price  + (avg_mid_price *  (config.midSpread /100)), config.ratePrecision)
    print(" percent down_sell_price ==> ", down_sell_price)

    print('==========')
    updatedBuyPrice = round((highest_buy_bid + 0.01),config.ratePrecision)
    print('updatedBuyPrice: ',updatedBuyPrice)
    updatedSellPrice = round((lowest_sell_bid - 0.01),config.ratePrecision)
    print('updatedSellPrice:',updatedSellPrice)

    print('==========')

    if orderbookSpread > config.bns_minimum_spread : #or avg_mid_price > coindcx_mid_price 
        print(' ====================>>> CANCEL OPEN ORDER <<<====================')
        bitbnsObj = bitbns(key, secretKey)
        try:
            openOrderList = bitbnsObj.listOpenOrders(symbol = config.INRpair)
            # print("openOrderList = = >", openOrderList)
            open_order_dump = json.dumps(openOrderList)
            open_order_load = json.loads(open_order_dump)
            for entry_ids in open_order_load['data']:
                # print('entry_ids = > ',entry_ids)
                Open_orders = entry_ids['entry_id']
                print('Cancelling Open order ====> ', Open_orders )
                cancel_open_orders  =  bitbnsObj.cancelOrder(symbol = config.INRpair, entry_id = Open_orders)
                print('cancel_open_orders ====> ', cancel_open_orders)
                time.sleep(5)
        except:
            print('No open orders')

        req = Request(
            url = "https://public.coindcx.com/market_data/trade_history?pair=I-"+ config.INRpair + "_INR&limit=1",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        CoinDCXRate = urlopen(req).read()
        # print(CoinDCXRate)

        data_json = json.loads(CoinDCXRate)
        # print("data_json ==> ",data_json)

        price = float(data_json[0]['p'])

        print('coindcx_price ===> ',price)
        coindcx_mid_price = float(price + ((price * config.CoinDCXrateSpreadPercent)/100))
        coindcx_mid_price = truncate(coindcx_mid_price,3 )
        print("coindcx_33_percent_up_mid_price == >", coindcx_mid_price)

        coindcx_buy_price = truncate( coindcx_mid_price  - (coindcx_mid_price *  (config.midSpread /100)), config.ratePrecision)
        print("coindcx_buy_price ==> ", coindcx_buy_price)
        coindcx_sell_price = truncate( coindcx_mid_price  + (coindcx_mid_price *  (config.midSpread /100)), config.ratePrecision)
        print("coindcx_sell_price ==> ", coindcx_sell_price)

        ticker = b.fetchTickers()
        insideData = ticker['data']
        eachCoins = insideData.keys()
        for pairs, pairData in insideData.items():
            if config.INRpair == pairs:
                highest_buy_bid = pairData.get('highest_buy_bid')
                print("highest_buy_bid: ", highest_buy_bid)
                lowest_sell_bid = pairData.get('lowest_sell_bid')
                print("lowest_sell_bid: ", lowest_sell_bid)

        print(' ====================>>> COMPARE BEST RATES <<<====================')
        if (coindcx_buy_price < highest_buy_bid):
            bestBuyRate = truncate(coindcx_buy_price,config.ratePrecision)
            print('bestBuyRate1 coindcx_buy_price: ', bestBuyRate)
        else:
            bestBuyRate = truncate(updatedBuyPrice,config.ratePrecision)
            print('bestBuyRate2 updatedBuyPrice : ', bestBuyRate)

        if (coindcx_sell_price > updatedSellPrice ):
            bestSellRate = truncate(coindcx_sell_price,config.ratePrecision)
            print('bestSellRate1 coindcx_sell_price: ', bestSellRate)
        else:
            bestSellRate = truncate(updatedSellPrice,config.ratePrecision)
            print('bestSellRate2 updatedSellPrice : ', bestSellRate)

    
        print(' ====================>>> GET BALANCES <<<====================')
        getAllCoinBalances = bitbnsObj.currentCoinBalance( config.INRpair)
        # print("getAllCoinBalances ===>", getAllCoinBalances)
        data_json_dump = json.dumps(getAllCoinBalances)
        data_json_load = json.loads(data_json_dump)
        # print("data_json_load ==> ",data_json_load)

        coin_free_bal = truncate(float(data_json_load['data']['availableorder'+config.INRpair]),config.quantityPrecision)
        print(config.INRpair,"_free_bal ==> ",coin_free_bal)
        inorderCoinBalance = float(data_json_load['data']['inorder'+config.INRpair])
        print(config.INRpair,"_inorder_bal ==> ",inorderCoinBalance)

        getBalancesINR = bitbnsObj.currentCoinBalance( 'INR')
        # print("BalancesINR ===>", getBalancesINR)
        data_json_dump = json.dumps(getBalancesINR)
        data_json_load = json.loads(data_json_dump)
        # print("data_json_load ****************==> ",data_json_load)

        inr_free_bal = float(data_json_load['data']['availableorderMoney'])
        print("inr_free_bal ==> ",inr_free_bal)
        inorderINR = float(data_json_load['data']['inorderMoney'])
        print("inorderINR ==> ",inorderINR)

        time.sleep(5)
        print(' ====================>>> place LIMIT SELL Order <<<====================')
        placeLimitSellOrder = bitbnsObj.placeSellOrder(symbol = config.INRpair, rate = bestSellRate, quantity = coin_free_bal)
        print('place Sell order data: ===>', placeLimitSellOrder)


        print(' ====================>>> place LIMIT BUY Order <<<====================')
        buyOrderFees = truncate((inr_free_bal * (0.25/100)),config.ratePrecision)
        print("buyOrderFees ==> ", buyOrderFees)
        buyOrderQuantity = truncate(((inr_free_bal - buyOrderFees)/bestBuyRate),config.quantityPrecision)
        print("buyOrderQuantity ===> ", buyOrderQuantity)

        time.sleep(5)
        placeLimitBuyOrder = bitbnsObj.placeBuyOrder(symbol = config.INRpair, rate = bestBuyRate, quantity = buyOrderQuantity)
        print('place Buy order data: ===>', placeLimitBuyOrder)
        print(datetime.datetime.now())
        print('SLEEP TIME: ',placedelay)
        del open_order_dump
        del open_order_load
        time.sleep(placedelay)
        print(datetime.datetime.now())
        print(' ====================>>> CYCLE COMPLETED <<<====================')
        print(' ====================>>> NEW CYCLE STARTS <<<====================')
    else:
        print("No order changes...")
        print(datetime.datetime.now())
        print('SLEEP TIME: ',placedelay)
        del open_order_dump
        del open_order_load
        time.sleep(placedelay)
        print(datetime.datetime.now())
