"""Provides the template methods that an expert must implement

Keeping this simple for now, doing what I think is best

Experts have to have an order manager passed for each of their methods

For further documentations see: https://www.mql5.com/en/docs/basis/function/events"""

import abc
from mqlpy.constants_enumerations_structures.trade_constants import Timeframes


class ExpertBase():
    __metaclass__ = abc.ABCMeta

    def __init__(self, ea_parameters=[], timeframe=Timeframes.PERIOD_M1):
        """Called upon the initalisation of the expert"""
        self.data_sources = None
        return

    @abc.abstractclassmethod
    def on_start(self, order_manager, ea_parameters, current_time):
        """Called when expert has been initialsied with an order manager and program manager successfully"""
        return

    @abc.abstractclassmethod
    def on_data(self, order_manager, data_buffer, current_time):
        """Called when new data has been received"""
        return

    @abc.abstractclassmethod
    def on_deinit(self, order_manager, data_buffer, current_time, reason):
        """Called upon the deinitialisation of the expert"""
        return

    @abc.abstractclassmethod
    def on_trade(self, order_manager, data_buffer, current_time):
        """Called when a new trade event occurs"""