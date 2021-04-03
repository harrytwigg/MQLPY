"""Provides the template methods that an order manager must implement

To use for demo test order managers without having to actually implement a
real conenction, but one could be easily connected to existing code

Keeping this simple for now, doing what I think is best"""

import abc


class OrderManagerBase():
    __metaclass__ = abc.ABCMeta

    def setCurrentDateTime(self, currentDateTime=None):
        """Optionally set the current dateTime for backtesting"""
        self.currentDateTime = currentDateTime

    @abc.abstractclassmethod
    def orderOpen(self, symbol, orderType, volume, stopLoss, takeProfit, typeTime, expiration, stopLimit, comment):
        """Places a pending order with specified parameters"""
        return
    
    @abc.abstractclassmethod
    def orderModify(self, ticket, price, stopLoss, takeProfit, typeTime, expiration, stopLimit):
        """Modifies a pending order parameters"""
        return
    
    @abc.abstractclassmethod
    def orderDelete(self, ticket):
        """Deletes a pending order"""
        return
    
    @abc.abstractclassmethod
    def buy(self, volume, symbol, price, stopLoss, takeProfit, comment):
        """Opens a long position with specified parameters"""
        return

    @abc.abstractclassmethod
    def sell(self, volume, symbol, price, stopLoss, takeProfit, comment):
        """Opens a short position with specified parameters"""
        return
    
    @abc.abstractclassmethod
    def positionClose(self, ticket, deviation):
        """Closes a position with the specified ticket"""
        return
    
    @abc.abstractclassmethod
    def positionClosePartial(self, ticket, volume, deviation):
        """Closes a position with the specified ticket"""
        return