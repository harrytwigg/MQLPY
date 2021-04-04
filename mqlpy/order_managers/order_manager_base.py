"""Provides the template methods that an order manager must implement

To use for demo test order managers without having to actually implement a
real conenction, but one could be easily connected to existing code

Keeping this simple for now, doing what I think is best"""

import abc


class OrderManagerBase():
    __metaclass__ = abc.ABCMeta

    def set_current_date_time(self, current_date_time=None):
        """Optionally set the current dateTime for backtesting"""
        self.current_date_time = current_date_time

    @abc.abstractclassmethod
    def order_open(self, symbol, orderType, volume, stop_loss, take_profit, type_time, expiration, stop_limit, comment):
        """Places a pending order with specified parameters"""
        return
    
    @abc.abstractclassmethod
    def order_modify(self, ticket, price, stop_loss, take_profit, type_time, expiration, stop_limit):
        """Modifies a pending order parameters"""
        return
    
    @abc.abstractclassmethod
    def order_delete(self, ticket):
        """Deletes a pending order"""
        return
    
    @abc.abstractclassmethod
    def buy(self, volume, symbol, price, stop_loss, take_profit, comment):
        """Opens a long position with specified parameters"""
        return

    @abc.abstractclassmethod
    def sell(self, volume, symbol, price, stop_loss, take_profit, comment):
        """Opens a short position with specified parameters"""
        return
    
    @abc.abstractclassmethod
    def position_close(self, ticket, deviation):
        """Closes a position with the specified ticket"""
        return
    
    @abc.abstractclassmethod
    def position_close_partial(self, ticket, volume, deviation):
        """Closes a position with the specified ticket"""
        return