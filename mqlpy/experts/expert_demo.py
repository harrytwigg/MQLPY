"""A demo expert advisor that tries to ipen 1 lot EUR/USD position then nothin more

Use event handlers to control the expert from the outside, autonomous code ie timers
inside the expert should avoided"""

import logging
from mqlpy.experts import ExpertBase
from mqlpy.constants_enumerations_structures.trade_constants import Timeframes
from mqlpy.constants_enumerations_structures.data_source_constants import *


class ExpertDemo(ExpertBase):
    def __init__(self, ea_parameters=[], timeframe=Timeframes.PERIOD_M1):
        """Constructor for when expert is created, not when it is started"""
        self.ea_parameters = ea_parameters
        self.timeframe = timeframe
        self.data_sources = {
            DataSource.ARCTIC_SOURCE: {
                "192.168.0.43": {
                    "libraries": {
                        "FX OHLC 1M": {
                            "EURUSD"
                        }
                    }
                }
            }
        }
    
    def on_start(self, order_manager, data_buffer, current_time):
        """Called when expert has been initialsied with an order manager and program manager successfully"""
        logging.info("The expert advisor ExpertDemo has been intialised at time:", current_time)

    def on_data(self, order_manager, data_buffer, current_time):
        """Called when new data has been received"""
        '''self.i += 1
        order_manager.buy(10, "EUR/USD")
        if self.i == 10:
            order_manager.position_close(2)'''
        print(len(data_buffer[0]))
