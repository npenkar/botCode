from bitbnspy import bitbns

import config
key = config.apiKey
secretKey = config.secret
b = bitbns(key, secretKey)

# b = bitbns('API_KEY', 'SECRET_KEY')
data = b.getTickerSocket(marketName = 'INR')
socket = data['socket']

@socket.event
def ticker(data):
    print(data)


@socket.event
def disconnect():
    print("Disconnected")