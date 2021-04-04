"""Predefined data structures inline with the MLQ5 naming conventions"""


class TradeRequest:
    """Interaction between the client terminal and a trade server for executing the order placing operation is performed using trade requests
    https://www.mql5.com/en/docs/constants/structures/mqltraderequest"""

    def __init__(self, action, symbol, volume, type, type_filling, magic=None, order=None, price=None, stop_limit=None, stop_loss=None, take_profit=None, deviation=None, type_time=None, expiration=None, comment=None, position=None, position_by=None):
        self.action = action
        self.magic = magic
        self.order = order
        self.symbol = symbol
        self.volume = volume
        self.price = price
        self.stop_limit = stop_limit
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.deviation = deviation
        self.type = type
        self.type_filling = type_filling
        self.type_time = type_time
        self.expiration = expiration
        self.comment = comment
        self.position = position
        self.position_by = position_by


class TradeResult:
    """As result of a trade request, a trade server returns data about the trade request processing result as a special predefined structure
    https://www.mql5.com/en/docs/constants/structures/mqltraderesult"""

    def __init__(self, retcode, deal, order, volume, price, bid, ask, comment, request_id, retcode_external):
        self.retcode = retcode
        self.deal = deal
        self.order = order
        self.volume = volume
        self.price = price
        self.bid = bid
        self.ask = ask
        self.comment = comment
        self.request_id = request_id
        self.retcode_external = retcode_external