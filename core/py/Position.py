from core.py.bitmex.bitmexApi import BitMEX


class Position:
    def __init__(self):
        # todo: change BitMEX singleton
        self.bitmex = BitMEX(test=True, api_key="mRFAH87bvrET5B7kJ1OQz3JX",
                             api_secret="auENVlHIN-qMGsNQB7ebm7qWGg_riiYh3yhdNPiMPKnb2Jvd")
        self.load_position()

    @property
    def quantity(self):
        return self.__quantity

    @property
    def leverage(self):
        return self.__leverage

    @property
    def crossMargin(self):
        return self.__crossMargin

    @property
    def avgEntryPrice(self):
        return self.__avgEntryPrice

    @property
    def avgCostPrice(self):
        return self.__avgCostPrice

    @property
    def liquidationPrice(self):
        return self.__liquidationPrice

    def get_position(self):
        return self.bitmex.position()

    def load_position(self):
        pos = self.bitmex.position()
        self.__quantity = pos['currentQty']
        self.__leverage = pos['leverage']
        self.__crossMargin = pos['crossMargin']
        self.__avgEntryPrice = pos['avgEntryPrice']
        self.__avgCostPrice = pos['avgCostPrice']
        self.__liquidationPrice = pos['liquidationPrice']


if __name__ == '__main__':
    position = Position()
    print("price: " + str(position.quantity))