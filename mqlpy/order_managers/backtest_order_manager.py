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
import logging


class BacktestOrderManager(OrderManagerBase):
    def __init__(self):
        self.order_tick_increment = 0
        self.currency_rates = CurrencyRates()

        self.open_positions = []
        self.closed_positions = []
        self.balance = 10000.00

    '''might remove as not required for CTrade like functionality
    def orderSend(self, request):
        if request.action == TradeRequestAction.TRADE_ACTION_DEAL:
            price = self.currency_rates.get_rate(
                "EUR", "USD", self.current_date_time)
            new_order_ticket = self.order_tick_increment
            print("New deal market order received assuming deal taken place and new position with ticket",
                  self.order_tick_increment, "is now open")
            self.orderBook.append(new_order_ticket)
            self.tradeRequestHistory.append(request)
            self.order_tick_increment += 1
            return TradeResult(retcode=TradeRetcode.TRADE_RETCODE_PLACED, order=new_order_ticket, volume=request.volume, price=price, deal=None, bid=None, ask=None, comment=None, requestId=None, retcodeExternal=None)
        # elif request.action == TradeRequestAction'''

    def buy(self, volume, symbol, price=None, stop_loss=None, take_profit=None, comment=None):
        """Opens a long position with specified parameters
        https://www.mql5.com/en/docs/standardlibrary/tradeclasses/ctrade/ctradebuy"""
        new_order_ticket = self.order_tick_increment
        self.order_tick_increment += 1
        if symbol == "EUR/USD":
            price = self.currency_rates.get_rate(
                "EUR", "USD", self.current_date_time)
        self.open_positions.append(
            Position(new_order_ticket, OrderType.ORDER_TYPE_BUY, volume, symbol, price, stop_loss, take_profit, comment))
        return

    def sell(self, volume, symbol, price=None, stop_loss=None, take_profit=None, comment=None):
        """Opens a short position with specified parameters
        https://www.mql5.com/en/docs/standardlibrary/tradeclasses/ctrade/ctradesell"""
        new_order_ticket = self.order_tick_increment
        self.order_tick_increment += 1
        if symbol == "EUR/USD":
            price = self.currency_rates.get_rate(
                "EUR", "USD", self.current_date_time)
        self.open_positions.append(
            Position(new_order_ticket, OrderType.ORDER_TYPE_SELL, volume, symbol, price, stop_loss, take_profit, comment))
        return

    def position_close(self, ticket, deviation=100000):
        """Closes a position with the specified ticket"""

        for i in self.open_positions:
            if i.ticket == ticket:
                if i.symbol == "EUR/USD":
                    closing_price = self.currency_rates.get_rate(
                        "EUR", "USD", self.current_date_time)
                    if i.orderType == OrderType.ORDER_TYPE_BUY:
                        profit = round(i.volume * 100000 *
                                       (closing_price - i.price), 2)
                    elif i.orderType == OrderType.ORDER_TYPE_SELL:
                        profit = round(i.volume * 100000 *
                                       (i.price - closing_price), 2)
                    self.balance += profit
                closed_position = i
                closed_position.setClosed(closing_price, profit)
                self.open_positions.remove(i)
                self.closed_positions.append(closed_position)
                logging.info("Position closed with profit", closed_position.profit)
                break
        return

    def position_close_partial(self, ticket, volume, deviation=100000):
        """Closes a position with the specified ticket"""
        return


class Position:
    """Position class for locally storing positions within the order manager"""

    def __init__(self, ticket, orderType, volume, symbol, price, stop_loss=None, take_profit=None, comment=None, type_time=None, expiration=None):
        self.ticket = ticket
        self.orderType = orderType
        self.volume = volume
        self.symbol = symbol
        self.price = price
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.comment = comment
        self.type_time = type_time
        self.expiration = expiration
    
    def setClosed(self, close_price, profit):
        self.close_price = close_price
        self.profit = profit
