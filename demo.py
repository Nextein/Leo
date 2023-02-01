from ib_insync import *

ib = IB()
# Create network socket connection with Trader Work Station
ib.connect('127.0.0.1', 7497, clientId=1)  # localhost port 7497

# clientId allows for multiple copmuters connecting to one account.

# contract = Contract(___)
contract = Forex('EURUSD')
# stock = Stock('AAPL', 'NASDAQ', 'USD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print(df)

market = ib.reqMktData(contract, '', False, False)

def onPendingTickers(tickers):
    print("pending ticker event received.")
    print(tickers)

ib.pendingTickersEvent += onPendingTickers


ib.run()  #necessary to run in loop