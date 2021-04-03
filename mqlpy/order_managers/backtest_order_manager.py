"""
A backtest fx order manager that gets rates at a current time and stores them in a local database
In a live instance this would be kept at least partially on a remote server

Backtest ability is entirely optional
"""

from os import close
from time import process_time
from mqlpy.constants_enumerations_structures.data_structures import *
from mqlpy.constants_enumerations_structures.trade_constants import *
from mqlpy.order_managers import OrderManagerBase
from forex_python.converter import CurrencyRates
from logging import *


class BacktestOrderManager(OrderManagerBase):
    def __init__(self):
        self.orderTicketIncrement = 0
        self.currencyRates = CurrencyRates()

        self.openPositions = []
        self.closedPositions = []
        self.balance = 10000.00

    '''might remove as not required for CTrade like functionality
    def orderSend(self, request):
        if request.action == TradeRequestAction.TRADE_ACTION_DEAL:
            price = self.currencyRates.get_rate(
                "EUR", "USD", self.currentDateTime)
            newOrderTicket = self.orderTicketIncrement
            print("New deal market order received assuming deal taken place and new position with ticket",
                  self.orderTicketIncrement, "is now open")
            self.orderBook.append(newOrderTicket)
            self.tradeRequestHistory.append(request)
            self.orderTicketIncrement += 1
            return TradeResult(retcode=TradeRetcode.TRADE_RETCODE_PLACED, order=newOrderTicket, volume=request.volume, price=price, deal=None, bid=None, ask=None, comment=None, requestId=None, retcodeExternal=None)
        # elif request.action == TradeRequestAction'''

    def buy(self, volume, symbol, price=None, stopLoss=None, takeProfit=None, comment=None):
        """Opens a long position with specified parameters
        https://www.mql5.com/en/docs/standardlibrary/tradeclasses/ctrade/ctradebuy"""
        newOrderTicket = self.orderTicketIncrement
        self.orderTicketIncrement += 1
        if symbol == "EUR/USD":
            price = self.currencyRates.get_rate(
                "EUR", "USD", self.currentDateTime)
        self.openPositions.append(
            Position(newOrderTicket, OrderType.ORDER_TYPE_BUY, volume, symbol, price, stopLoss, takeProfit, comment))
        return

    def sell(self, volume, symbol, price=None, stopLoss=None, takeProfit=None, comment=None):
        """Opens a short position with specified parameters
        https://www.mql5.com/en/docs/standardlibrary/tradeclasses/ctrade/ctradesell"""
        newOrderTicket = self.orderTicketIncrement
        self.orderTicketIncrement += 1
        if symbol == "EUR/USD":
            price = self.currencyRates.get_rate(
                "EUR", "USD", self.currentDateTime)
        self.openPositions.append(
            Position(newOrderTicket, OrderType.ORDER_TYPE_SELL, volume, symbol, price, stopLoss, takeProfit, comment))
        return

    def positionClose(self, ticket, deviation=100000):
        """Closes a position with the specified ticket"""

        for i in self.openPositions:
            if i.ticket == ticket:
                if i.symbol == "EUR/USD":
                    closingPrice = self.currencyRates.get_rate(
                        "EUR", "USD", self.currentDateTime)
                    if i.orderType == OrderType.ORDER_TYPE_BUY:
                        profit = round(i.volume * 100000 *
                                       (closingPrice - i.price), 2)
                    elif i.orderType == OrderType.ORDER_TYPE_SELL:
                        profit = round(i.volume * 100000 *
                                       (i.price - closingPrice), 2)
                    self.balance += profit
                closedPosition = i
                closedPosition.setClosed(closingPrice, profit)
                self.openPositions.remove(i)
                self.closedPositions.append(closedPosition)
                info("Position closed with profit", closedPosition.profit)
                break
        return

    def positionClosePartial(self, ticket, volume, deviation=100000):
        """Closes a position with the specified ticket"""
        return


class Position:
    """Position class for locally storing positions within the order manager"""

    def __init__(self, ticket, orderType, volume, symbol, price, stopLoss=None, takeProfit=None, comment=None, typeTime=None, expiration=None):
        self.ticket = ticket
        self.orderType = orderType
        self.volume = volume
        self.symbol = symbol
        self.price = price
        self.stopLoss = stopLoss
        self.takeProfit = takeProfit
        self.comment = comment
        self.typeTime = typeTime
        self.expiration = expiration
    
    def setClosed(self, closePrice, profit):
        self.closePrice = closePrice
        self.profit = profit
