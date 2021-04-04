"""Program entry"""

from datetime import datetime
from mqlpy.constants_enumerations_structures.trade_constants import Timeframes
from mqlpy.program_managers import BacktestProgramManager
from mqlpy.experts import ExpertDemo
from mqlpy.order_managers import BacktestOrderManager
import logging


logging.basicConfig(level=logging.DEBUG)
start_date = datetime(2020, 1, 1)
order_manager = BacktestOrderManager()
expert = ExpertDemo(order_manager, )
program_manager = BacktestProgramManager(
    order_manager, expert, start_date, Timeframes.PERIOD_M1)
