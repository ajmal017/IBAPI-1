# https://www.youtube.com/watch?v=aSdi667LGp0
# IB API TWS Python API - Receiving Market Data and Historical
# Author: David Tsang
# GitHub: https://davidtsanghw.github.io
# 22 May 2020

# TERM OF USE
#
# VERY IMPORTANT!!!!
#
# TRADER WORK STATION (TWS) MUST BE LOGGED IN SUCCESSFULY WHEN RUNNING THIS PROGRAM
#
# MAKE SURE YOU ARE CONNECTING A PAPER ACCOUNT WHEN TEST AND DEBUGGING
#
# THE AUTHOR ACCEPTS NO RESPONSIBILITY FOR THE USE OF THIS PROGRAM. USE OF THIS PROGRAM IS ENTIRELY AT THE USER'S OWN RISK

# This program is in Python 3.7

# Prerequisites
# 1. Download and install TWS
# 2. Download and install IB API
# 3. Configure TWS

# Configure TWS 
# TWS > Global Configuration > API > Settings >
# 1. Enable Active X and Socket Clients > Enable
# 2. Socket port: 7497
# 3. Allow connections from localhost only > Disable
# 4. Allow connections from localhost only > Trusted IPs > Create > Enter 127.0.0.1
#
# ******  3 and 4 disable confirmation when connecting TWS  

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import Contract
from ibapi.order import *
from ibapi.ticktype import TickTypeEnum

from threading import Thread
import queue
import datetime
import time
import math

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self,reqId,errorCode,errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def tickPrice(self,reqId,tickType,price,attrib):
        print("Tick Price. Ticker Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Price:",price,end= ' ')        

    def tickSize(self,reqId,tickType,size):
        print("Tick Size. Ticker Id:",reqId,"tickType:",TickTypeEnum.to_str(tickType),"Size:",size)

def main():
    app = TestApp()  

    app.connect("127.0.0.1", 7497, 0)

    contract = Contract()
    contract.symbol = "MSFT"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    app.reqMarketDataType(4)
    app.reqMktData(1,contract,"",False,False,[])
    
    app.run()


if __name__ == '__main__':
    main()

    
