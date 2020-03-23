from core.py.bitmex.bitmexApi import BitMEX


# used response keys
# 'orderID': '39a603e6-3fc5-145f-570b-f4c05d8bb699'
# 'side': 'Sell'
# 'orderQty': 1000
# 'price': 7000
# 'leavesQty': 1000
# 'cumQty': 0
class MyOrder:
    def __init__(self):
        # todo: change BitMEX singleton
        self.bitmex = BitMEX(test=True, api_key="mRFAH87bvrET5B7kJ1OQz3JX",
                             api_secret="auENVlHIN-qMGsNQB7ebm7qWGg_riiYh3yhdNPiMPKnb2Jvd")
        self.load_my_order()

    @property
    def orders(self):
        return self.__orders

    def get_my_orders(self):
        return self.bitmex.open_order()

    def load_my_order(self):
        self.__orders = self.bitmex.open_order()

    def cancel_order(self, order_id):
        return self.bitmex.cancel_order(order_id)

    def cancel_all(self):
        return self.bitmex.cancel_all_orders()


if __name__ == '__main__':
    my_order = MyOrder()
    print("myorder: " + str(my_order.get_my_orders()))
    print("cancel: " + str(my_order.cancel_all()))
