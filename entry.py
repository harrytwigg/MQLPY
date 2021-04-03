"""Program entry"""

from datetime import datetime
from mqlpy.constants_enumerations_structures.trade_constants import DataInterval
from dateutil.relativedelta import relativedelta

from mqlpy.program_managers import BacktestProgramManager
from mqlpy.experts import ExpertDemo
from mqlpy.order_managers import BacktestOrderManager
import pytz

timezone = pytz.timezone("ETC/UTC")
start_date = datetime(2020, 1, 1)
order_manager = BacktestOrderManager()
expert = ExpertDemo(order_manager)
program_manager = BacktestProgramManager(order_manager, expert, start_date, DataInterval.M1)
