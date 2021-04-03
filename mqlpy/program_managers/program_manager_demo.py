"""
A demo program manager that launches a demo expert with a demo order manager

Program managers shall not be inherited due to their changing nature
"""

from mqlpy.constants_enumerations_structures.trade_constants import DataInterval
from datetime import datetime
from dateutil.relativedelta import relativedelta

from mqlpy.order_managers.backtest_order_manager import BacktestOrderManager
from mqlpy.experts.expert_demo import ExpertDemo

orderManager = BacktestOrderManager()
expertDemo = ExpertDemo(orderManager)

currentDate = datetime.datetime.utcnow() - relativedelta(years=1) # Set start date to 1 year ago
orderManager.setCurrentDateTime(datetime.utcnow())
expertDemo.onData(orderManager, 1, DataInterval.UNKNOWN)
while(True):
    orderManager.setCurrentDateTime(datetime.datetime.utcnow())
    print(currentDate)
    currentDate = currentDate + relativedelta(days=1)
    if currentDate > datetime.datetime.utcnow():
        break
