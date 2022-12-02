import json
import requests
from websocket import create_connection

r = requests.get("websocet")
# print((r.json()))
print((r.json()['token']))
token=(r.json()['token'])
userid=r.json()["quantBotUserId"]
message={ "quantBotUserId":userid, "token":token, "type":"Login"}
send=json.dumps(message)
# print(send)
# print(type(send))

def worker(cur,tradetrakerq,price_control):
    global reader,j
    httpsell='http://localhost:8001/order/place?Side=Sell&Qty=20000&Symbol='+cur
    httpbuy = 'http://localhost:8001/order/place?Side=Buy&Qty=20000&Symbol=' + cur
    rev = requests.get("http://localhost:8001/account/status")
    if reader["type"] == "GaugeUpdate" and "Symbol" in reader:# and rev.json()['OpenQuantity']==0:

        # print(tradetraker )
        if tradetrakerq == 0 and reader["Symbol"] == cur:
            # print("HEEEEEEEEEy")
            print(reader["Symbol"])
            if reader["EntryProgress"] > 0.76:
                print(reader)
                r = requests.get(httpsell)
                tradetrakerq = 1

                price_control=reader["Price"]


            elif reader["EntryProgress"] <- 0.76:
                r = requests.get(httpbuy)
                tradetrakerq = 2
                print(reader)
                price_control=reader["Price"]

            # print((r.json()))
            # print((r.json()['AvailableFunds']))
    if reader["type"] == "PriceUpdate" or (reader["type"] == "GaugeUpdate" and "Symbol" in reader) :
        if reader["type"] == "PriceUpdate":
            pricer=reader["LastPrice"]
        else:
            pricer = reader["Price"]
        if reader["Symbol"] == cur:

            if tradetrakerq == 1:
                # print("got it")
                price_diff = price_control - pricer
                # print(1)
                # print(price_diff)
                if price_diff >= 0.0005:
                    r = requests.get(httpbuy)
                    tradetrakerq = 0
                    price_control=0
                    print(price_diff)
                elif price_diff <= -0.0005:
                    r = requests.get(httpbuy)
                    tradetrakerq = 0
                    price_control = 0
                    print(price_diff)
                # print((r.json()))
                # print((r.json()['AvailableFunds']))
            elif tradetrakerq == 2:

                # print(reader)
                # print((r.json()))
                # print((r.json()['AvailableFunds']))
                price_diff = pricer - price_control
                # print(2)
                # print(price_diff)
                if price_diff >= 0.0005:
                    r = requests.get(httpsell)
                    tradetrakerq = 0
                    price_control = 0
                    print(price_diff)
                elif price_diff <= -0.0005:
                    r = requests.get(httpsell)
                    tradetrakerq = 0
                    price_control = 0
                    print(price_diff)

                # print((r.json()))
                # print((r.json()['AvailableFunds']))

    if reader["type"] == "OrderExecution" and tradetrakerq != 0 and reader["Symbol"] == cur and reader["exit"] == "True":
        print("HEEEEEEEEEy")
        if reader["executionType"] == "SELL":
            r = requests.get(httpbuy)
            tradetrakerq = 0
            price_control = 0
        else:
            r = requests.get(httpsell)
            tradetraker = 0
            price_control = 0
    # print(price_control)
    return(tradetrakerq,price_control)

ws = create_connection("Web socket")
ws.send(send)
result = ws.recv()
print(result)
i=1
j=0
tradetraker=0
price_control=0
tradetraker1=0
price_control1=0
tradetraker2=0
price_control2=0
while True:
    result =ws.recv()
    reader=json.loads(result)
    # print(tradetraker)
    if reader["type"]=="GaugeUpdate"and "Symbol" in reader:
        pass
        # print(result)
    result=worker("USD.CAD",tradetraker,price_control)
    tradetraker=result[0]
    price_control=result[1]

    result=worker("EUR.USD",tradetraker1,price_control1)
    tradetraker1=result[0]
    price_control1=result[1]

    result=worker("GBP.USD",tradetraker2,price_control2)
    tradetraker2=result[0]
    price_control2=result[1]
    # r = requests.get("http://localhost:8001/account/status")
    # print((r.json())[])
    # print(reader)
    if reader["type"] == "GaugeUpdate":
        # if reader["EntryProgress"]<-0.77 or reader["EntryProgress"]>0.77:
            print(reader["Symbol"])

