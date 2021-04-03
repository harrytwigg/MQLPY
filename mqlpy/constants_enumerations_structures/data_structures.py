"""Predefined data structures inline with the MLQ5 naming conventions"""


class TradeRequest:
    """Interaction between the client terminal and a trade server for executing the order placing operation is performed using trade requests
    https://www.mql5.com/en/docs/constants/structures/mqltraderequest"""

    def __init__(self, action, symbol, volume, type, typeFilling, magic=None, order=None, price=None, stopLimit=None, stopLoss=None, takeProfit=None, deviation=None, typeTime=None, expiration=None, comment=None, position=None, positionBy=None):
        self.action = action
        self.magic = magic
        self.order = order
        self.symbol = symbol
        self.volume = volume
        self.price = price
        self.stopLimit = stopLimit
        self.stopLoss = stopLoss
        self.takeProfit = takeProfit
        self.deviation = deviation
        self.type = type
        self.typeFilling = typeFilling
        self.typeTime = typeTime
        self.expiration = expiration
        self.comment = comment
        self.position = position
        self.positionBy = positionBy


class TradeResult:
    """As result of a trade request, a trade server returns data about the trade request processing result as a special predefined structure
    https://www.mql5.com/en/docs/constants/structures/mqltraderesult"""

    def __init__(self, retcode, deal, order, volume, price, bid, ask, comment, requestId, retcodeExternal):
        self.retcode = retcode
        self.deal = deal
        self.order = order
        self.volume = volume
        self.price = price
        self.bid = bid
        self.ask = ask
        self.comment = comment
        self.requestId = requestId
        self.retcodeExternal = retcodeExternal