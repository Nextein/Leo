from ib_insync import *
from pprint import pprint

ib = IB()
# Create network socket connection with Trader Work Station
ib.connect('127.0.0.1', 7497, clientId=1)  # localhost port 7497




contract = Forex('EURGBP')
# stock = Stock('AAPL', 'NASDAQ', 'USD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='1 M',
    barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print(df)
exit()





# ================= CREATE STOCK LIST FOR STOCKS (REQUIRES DATA SUBSCRIPTION)
letters = 'BC'  # For quick testing
# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# symbols = []
# for l in letters:
#     print(l)
#     symbols += ib.reqMatchingSymbols(l)
# stocks = [symbol for symbol in symbols if symbol.contract.secType=='STK']


# ================ CREATE FOREX LIST FOR STOCKS (DOESN'T REQUIRE API. USING THIS FOR NOW)
tradedpairs = ['AUDCAD','AUDCHF','AUDJPY','AUDNZD','AUDUSD','CADCHF','CADJPY','CHFJPY','EURAUD','EURCAD','EURCHF','EURGBP','EURJPY','EURNZD','EURUSD','GBPAUD','GBPCAD','GBPCHF','GBPJPY','GBPNZD','GBPUSD','NZDCAD','NZDCHF','NZDJPY','NZDUSD','USDCAD','USDCHF','USDJPY']
stocks = []
for pair in tradedpairs:
    print(pair)
    stocks += [Forex(pair)]



# allbars = {}

# for stock in stocks:
#     print(stock.contract.symbol)
#     try:
#         bars = ib.reqHistoricalData(
#             stock.contract,
#             endDateTime='',
#             durationStr='1 M',
#             barSizeSetting='1 hour',
#             whatToShow='TRADES',
#             useRTH=True
#         )
#         allbars[stock.contract.symbol] = bars


#     except AttributeError as e:
#         continue

# print(allbars)

# i=0

for i in range(len(stocks)):


    bars = ib.reqHistoricalData(
        stocks[i],
        endDateTime='',
        durationStr='50 D',
        barSizeSetting='1 day',
        whatToShow='TRADES',
        useRTH=True
    )

    # ib.sleep(1)  # What is necessary for reqHistoricalData() request?

    print(bars)



exit()





# clientId allows for multiple copmuters connecting to one account.

# contract = Contract(___)
contract = Forex('EURUSD')
# stock = Stock('AAPL', 'NASDAQ', 'USD')
bars = ib.reqHistoricalData(
    stocks[0], endDateTime='', durationStr='1 M',
    barSizeSetting='1 hour', whatToShow='TRADES', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print(df)





exit()








market = ib.reqMktData(contract, '', False, False)

def onPendingTickers(tickers):
    print("pending ticker event received.")
    print(tickers)

ib.pendingTickersEvent += onPendingTickers


ib.run()  #necessary to run in loop

