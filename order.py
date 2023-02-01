from ib_insync import *

ib = IB()
# Create network socket connection with Trader Work Station
ib.connect('127.0.0.1', 7497, clientId=1)  # localhost port 7497

# clientId allows for multiple copmuters connecting to one account.

# contract = Contract(___)
contract = Stock('AMD', 'SMART', 'USD')

order = MarketOrder('BUY', 1)

trade = ib.placeOrder(contract, order)

def orderFilled(order, fill):
    print("Order submitted")
    print(order)
    print(fill)

trade.fillEvent += orderFilled


ib.run()