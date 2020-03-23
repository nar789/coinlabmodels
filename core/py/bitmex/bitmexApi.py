# All bitmex api python file is putted in this folder
import requests
from core.py.bitmex.auth import APIKeyAuthWithExpires
from core.py.bitmex.ws.bitmexWebsocket import BitMEXWebsocket


# https://www.bitmex.com/api/explorer/
class BitMEX(object):

    def __init__(self, test=True, api_key=None, api_secret=None, postOnly=False):
        if (api_key is None):
            raise Exception("Please set an API key and Secret to get started. See " +
                            "https://github.com/BitMEX/sample-market-maker/#getting-started for more information.")

        self.symbol = 'XBTUSD'
        self.api_key = api_key
        self.api_secret = api_secret
        self.postOnly = postOnly

        if test:
            host = 'https://testnet.bitmex.com'
        else:
            host = 'https://www.bitmex.com'

        self.base_url = host + "/api/v1/"
        self.orderIDPrefix = "mm_bitmex_"

        # Prepare Https session
        self.session = requests.Session()
        self.timeout = 7

        # prepare websocket connection
        self.ws = BitMEXWebsocket(endpoint=self.base_url, symbol=self.symbol, api_key=self.api_key,
                                  api_secret=self.api_secret)

    def __del__(self):
        self.exit()

    def exit(self):
        self.ws.exit()

    def ticker_data(self):
        return self.ws.get_ticker()

    def place_order(self, price, quantity):
        if price < 0:
            raise Exception("Price must be positive.")

        endpoint = "order"
        # clientOrderID = self.orderIDPrefix + base64.b64encode(uuid.uuid4().bytes).decode('utf8').rstrip('=\n')
        postdict = {
            'symbol': self.symbol,
            'orderQty': quantity,
            'price': price
            # 'clOrdID':clientOrderID
        }
        return self._REST_reqeust(path=endpoint, postdict=postdict, verb="POST")

    def position(self):
        return self.ws.positions(self.symbol)

    def _REST_reqeust(self, path, query=None, postdict=None, timeout=None, verb=None,
                      rethrow_error=False, max_retries=None):
        url = self.requestUrl + path
        print(url)

        if timeout is None:
            timeout = self.timeout

        if not verb:
            verb = 'POST' if postdict else 'GET'

        if max_retries is None:
            max_retries = 10

        auth = APIKeyAuthWithExpires(self.api_key, self.api_secret)

        response = None
        try:
            req = requests.Request(verb, url, json=postdict, auth=auth, params=query)
            prep_request = self.session.prepare_request(req)
            response = self.session.send(prep_request, timeout=timeout)

            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            if response is None:
                raise e

        return response.json()

# mRFAH87bvrET5B7kJ1OQz3JX
# auENVlHIN-qMGsNQB7ebm7qWGg_riiYh3yhdNPiMPKnb2Jvd
if __name__ == "__main__":
    print("test")
    bitmex = BitMEX(api_key="mRFAH87bvrET5B7kJ1OQz3JX", api_secret="auENVlHIN-qMGsNQB7ebm7qWGg_riiYh3yhdNPiMPKnb2Jvd")
    response = bitmex.ticker_data()
    print(response)