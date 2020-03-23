from core.py.bitmex.bitmexApi import BitMEX


# 1.By using bitmaxAPI, get current BTC price.

class Coin:
    def __init__(self):
        # todo: change BitMEX singleton
        self.bitmex = BitMEX(test=True, api_key="mRFAH87bvrET5B7kJ1OQz3JX",
                             api_secret="auENVlHIN-qMGsNQB7ebm7qWGg_riiYh3yhdNPiMPKnb2Jvd")

    def get_price(self):
        return self.bitmex.ticker_data()['last']


if __name__ == '__main__':
    coin = Coin()
    print("price: " + str(coin.get_price()))
