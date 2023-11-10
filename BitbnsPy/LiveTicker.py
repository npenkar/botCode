import json
from bitbnspy import bitbns

bitbnsObj = bitbns.publicEndpoints()

# Pass ALL as coin name to get orderbook of all coins
# Pass USDT as market name to get orderbook of USDT market

data = bitbnsObj.getOrderBookSocket(coinName = 'MATIC', marketName = 'INR')
socket = data['socket']
print("a")

@socket.event
def news(data):
    print(data)
    response_dict = json.loads(data)
    data_string = response_dict['data']
    data_list = json.loads(data_string)

    for item in data_list:
        print("Rate:", item['rate'])
        print("BTC:", item['btc'])
        print()

print("================")



# Parse the 'data' string again to get a list of dictionaries







    # print("type of data==> ",type(data))
    # abc = data[0][1]
    # print("abc -=====> ",abc)

    # print("after socket listened")
    # if "type" == "buyList":

    # insideData = data[0]
    # print("type: ===>", insideData)

@socket.event
def disconnect():
    print("Disconnected")