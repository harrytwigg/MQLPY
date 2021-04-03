"""Provides the template methods that an expert must implement

Keeping this simple for now, doing what I think is best

Experts have to have an order manager passed for each of their methods

For further documentations see: https://www.mql5.com/en/docs/basis/function/events"""

import abc

from mqlpy.constants_enumerations_structures.trade_constants import DataInterval

class ExpertBase():
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def __init__(self, order_manager, ea_parameters):
        """Called upon the initalisation of the expert"""
        self.data_sources = None
        return

    @abc.abstractclassmethod
    def onData(self, order_manager, data_buffer, data_interval=DataInterval.UNKNOWN):
        """Called when new data has been received"""
        return

    @abc.abstractclassmethod
    def onDeinit(self, order_manager, data_buffer, reason):
        """Called upon the deinitialisation of the expert"""
        return

    @abc.abstractclassmethod
    def onTrade(self, order_manager, data_buffer):
        """Called when a new trade event occurs"""