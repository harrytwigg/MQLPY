"""A demo expert advisor that tries to ipen 1 lot EUR/USD position then nothin more

Use event handlers to control the expert from the outside, autonomous code ie timers
inside the expert should avoided"""


from logging import *

from mqlpy.experts import ExpertBase
from mqlpy.constants_enumerations_structures.data_structures import TradeRequest
from mqlpy.constants_enumerations_structures.trade_constants import OrderTypeFilling, TradeRequestAction, DataInterval
from mqlpy.constants_enumerations_structures.data_source_constants import *

class ExpertDemo(ExpertBase):
    def __init__(self, order_manager):
        info("The expert advisor ExpertDemo has been intialised!")
        self.data_sources = {
            DataSource.ARCTIC_SOURCE: {
                "192.168.0.43": {
                    "libraries": {
                        "FX OHLCs": {
                            "EURUSD 1M"
                        }
                    }
                }
            }
        }

    def onData(self, order_manager, data_buffer, data_interval=DataInterval.UNKNOWN):
        self.i += 1
        order_manager.buy(10, "EUR/USD")
        if self.i == 10:
            order_manager.positionClose(2)
