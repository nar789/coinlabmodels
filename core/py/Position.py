from bitmex.bitmexApi import BitMEX


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
    print("price: " + str(position.get_position()))
    # output
    # price: {'account': 287919, 'symbol': 'XBTUSD', 'currency': 'XBt', 'underlying': 'XBT', 'quoteCurrency': 'USD', 'commission': 0.00075, 'initMarginReq': 0.01, 'maintMarginReq': 0.0045000000000000005, 'riskLimit': 20000000000, 'leverage': 100, 'crossMargin': True, 'deleveragePercentile': 1, 'rebalancedPnl': 230254, 'prevRealisedPnl': 0, 'prevUnrealisedPnl': 0, 'prevClosePrice': 7670.39, 'openingTimestamp': '2020-04-26T14:00:00.000Z', 'openingQty': 3, 'openingCost': -47805, 'openingComm': -55, 'openOrderBuyQty': 0, 'openOrderBuyCost': 0, 'openOrderBuyPremium': 0, 'openOrderSellQty': 0, 'openOrderSellCost': 0, 'openOrderSellPremium': 0, 'execBuyQty': 0, 'execBuyCost': 0, 'execSellQty': 0, 'execSellCost': 0, 'execQty': 0, 'execCost': 0, 'execComm': 0, 'currentTimestamp': '2020-04-26T14:48:10.303Z', 'currentQty': 3, 'currentCost': -47805, 'currentComm': -55, 'realisedCost': 0, 'unrealisedCost': -47805, 'grossOpenCost': 0, 'grossOpenPremium': 0, 'grossExecCost': 0, 'isOpen': True, 'markPrice': 7637.79, 'markValue': -39279, 'riskValue': 39279, 'homeNotional': 0.00039279, 'foreignNotional': -3, 'posState': '', 'posCost': -47805, 'posCost2': -45821, 'posCross': 1984, 'posInit': 479, 'posComm': 38, 'posLoss': 1984, 'posMargin': 517, 'posMaint': 254, 'posAllowance': 0, 'taxableMargin': 0, 'initMargin': 0, 'maintMargin': 9043, 'sessionMargin': 0, 'targetExcessMargin': 0, 'varMargin': 0, 'realisedGrossPnl': 0, 'realisedTax': 0, 'realisedPnl': 55, 'unrealisedGrossPnl': 8526, 'longBankrupt': 0, 'shortBankrupt': 0, 'taxBase': 0, 'indicativeTaxRate': None, 'indicativeTax': 0, 'unrealisedTax': 0, 'unrealisedPnl': 8526, 'unrealisedPnlPcnt': 0.1783, 'unrealisedRoePcnt': 17.835, 'simpleQty': None, 'simpleCost': None, 'simpleValue': None, 'simplePnl': None, 'simplePnlPcnt': None, 'avgCostPrice': 6275.5, 'avgEntryPrice': 6275.5, 'breakEvenPrice': 1079, 'marginCallPrice': 235, 'liquidationPrice': 235, 'bankruptPrice': 235, 'timestamp': '2020-04-26T14:48:10.303Z', 'lastPrice': 7637.79, 'lastValue': -39279}