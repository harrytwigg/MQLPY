"""Various constants used for programming trading strategies"""

from enum import Enum

class TradeRequestAction(Enum):
    """Each trade order refers to the type of the requested operation
    https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions"""
    TRADE_ACTION_DEAL = 0
    TRADE_ACTION_PENDING = 1
    TRADE_ACTION_SLTP = 2
    TRADE_ACTION_MODIFY = 3
    TRADE_ACATION_REMOVE = 4


class OrderType(Enum):
    """When sending a trade request, some operations require an order type
    https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_type"""
    ORDER_TYPE_BUY = 0
    ORDER_TYPE_SELL = 1
    ORDER_TYPE_BUY_LIMIT = 2
    ORDER_TYPE_SELL_LIMIT = 3
    ORDER_TYPE_BUY_STOP = 4
    ORDER_TYPE_SELL_STOP = 5
    ORDER_TYPE_BUY_STOP_LIMIT = 6
    ORDER_TYPE_SELL_STOP_LIMIT = 7
    ORDER_TYPE_CLOSE_BY = 8


class OrderTypeFilling(Enum):
    """The trade request filling policy can be set when sending a trade request
    https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_type_filling"""
    ORDER_FILLING_FOK = 0
    ORDER_FILLING_IOC = 1
    ORDER_FILLING_RETURN = 2


class OrderTypeTime(Enum):
    """Specify the order validity period
    https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_type_time"""
    ORDER_TIME_GTC = 0
    ORDER_TIME_DAY = 1
    ORDER_TIME_SPECIFIED = 2
    ORDER_TIME_SPECIFIED_DAY = 3


class OrderState(Enum):
    """Each order has a status that describes its state
    https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_state"""


class TradeRetcode(Enum):
    """Trade server return codes for the TradeResult object returned upon a trade request
    https://www.mql5.com/en/docs/constants/errorswarnings/enum_trade_return_codes"""
    TRADE_RETCODE_REQUOTE = 10004
    TRADE_RETCODE_REJECT = 10006
    TRADE_RETCODE_CANCEL = 10007
    TRADE_RETCODE_PLACED = 10008
    TRADE_RETCODE_DONE = 10009
    TRADE_RETCODE_DONE_PARTIAL = 10010
    TRADE_RETCODE_ERROR = 10011
    TRADE_RETCODE_TIMEOUT = 10012
    TRADE_RETCODE_INVALID = 10013
    TRADE_RETCODE_INVALID_VOLUME = 10014
    TRADE_RETCODE_INVALID_PRICE = 10015
    TRADE_RETCODE_INVALID_STOPS = 10016
    TRADE_RETCODE_TRADE_DISABLED = 10017
    TRADE_RETCODE_MARKET_CLOSED = 10018
    TRADE_RETCODE_NO_MONEY = 10019
    TRADE_RETCODE_PRICE_CHANGED = 10020
    TRADE_RETCODE_PRICE_OFF = 10021
    TRADE_RETCODE_INVALID_EXPIRATION = 10022
    TRADE_RETCODE_ORDER_CHANGED = 10023
    TRADE_RETCODE_TOO_MANY_REQUESTS = 10024
    TRADE_RETCODE_NO_CHANGES = 10025
    TRADE_RETCODE_SERVER_DISABLES_AT = 10026
    TRADE_RETCODE_CLIENT_DISABLES_AT = 10027
    TRADE_RETCODE_LOCKED = 10028
    TRADE_RETCODE_FROZEN = 10029
    TRADE_RETCODE_INVALID_FILL = 10030
    TRADE_RETCODE_CONNECTION = 10031
    TRADE_RETCODE_ONLY_REAL = 10032
    TRADE_RETCODE_LIMIT_ORDERS = 10033
    TRADE_RETCODE_LIMIT_VOLUME = 10034
    TRADE_RETCODE_INVALID_ORDER = 10035
    TRADE_RETCODE_POSITION_CLOSED = 10036
    TRADE_RETCODE_INVALID_CLOSE_VOLUME = 10038
    TRADE_RETCODE_CLOSE_ORDER_EXIST = 10039
    TRADE_RETCODE_LIMIT_POSITIONS = 10040
    TRADE_RETCODE_REJECT_CANCEL = 10041
    TRADE_RETCODE_LONG_ONLY = 10042
    TRADE_RETCODE_SHORT_ONLY = 10043
    TRADE_RETCODE_CLOSE_ONLY = 10044
    TRADE_RETCODE_FIFO_CLOSE = 10045
    TRADE_RETCODE_HEDGE_PROHIBITED = 10046


class DataInterval(Enum):
    """Data intervals to classify new data by timeframe"""
    UNKNOWN = 0
    TICK = 1
    M1 = 2
    M5 = 3
    M15 = 4
