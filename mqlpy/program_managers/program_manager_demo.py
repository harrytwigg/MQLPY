"""
A demo program manager that launches a demo expert with a demo order manager

Program managers shall not be inherited due to their changing nature
"""

from mqlpy.constants_enumerations_structures.trade_constants import Timeframes
from datetime import datetime
from dateutil.relativedelta import relativedelta
from mqlpy.order_managers.backtest_order_manager import BacktestOrderManager
from mqlpy.experts.expert_demo import ExpertDemo


orderManager = BacktestOrderManager()
expertDemo = ExpertDemo(orderManager)

# Set start date to 1 year ago
current_time = datetime.utcnow() - relativedelta(years=1)
orderManager.setCurrentDateTime(datetime.utcnow())
expertDemo.onData(orderManager, 1, Timeframes.PERIOD_M1)

while(True):
    orderManager.setCurrentDateTime(datetime.datetime.utcnow())
    print(current_time)
    current_time = current_time + relativedelta(days=1)
    if current_time > datetime.datetime.utcnow():
        break
