from ib_insync import *

ib = IB()

ib.connect('127.0.0.1', 7497, clientId=1)

subscription = ScannerSubscription(
    instrument='STK',
    locationCode='STK.US.MAJOR'
)

scanData = ib.reqScannerData(subscription)

for scan in scanData:
    # print(scan)
    print(scan.contractDetails.contract.symbol)
