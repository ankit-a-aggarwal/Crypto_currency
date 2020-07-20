import importlib
import logging

import ccxt

importlib.reload(logging)
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.
                    INFO)

# FIELDS
PRICE = 'PRICE'
HIGH = 'HIGH24HOUR'
LOW = 'LOW24HOUR'
VOLUME = 'VOLUME24HOUR'
CHANGE = 'CHANGE24HOUR'
CHANGE_PERCENT = 'CHANGEPCT24HOUR'
MARKETCAP = 'MKTCAP'
NPERIODS = 100
TIMEFRAME = 'Day'
datetimeStringformat_to_csv = "%d-%m-%Y %H:%M"
data_directory = '/Users/ankitaggarwal/Applications/Cryptocurrency Trading System/crypto-analysis/data/'

CURR = 'BTC'
EXCHANGE = 'CCCAGG'
COIN = 'ETH'
COIN_LIST = ['BTC', 'ETH']
EXCHANGES = ['Bittrex','Binance']
EXCHANGES = ['Binance']

bittrex_exchange = ccxt.bittrex()
binance_exchange = ccxt.binance()
coinbasePro = ccxt.coinbasepro()
list_of_exchanges = [coinbasePro]

def setupExchanges(list_of_exchanges):
    done = False
    i=0
    #df_markets = pd.DataFrame(markets)
    #bittrex_market = bittrex_exchange.fetchMarkets()
    #binance_market = binance_exchange.fetchMarkets()
    #kucoin_market = kucoin_exchange.fetchMarkets()
    #list_of_markets = [#bittrex_market,
                       #binance_market
     #                  kucoin_market #For kucoin the fetchMarkets function returns different dictionary keys
      #                  ]

    list_of_tuples = []
    for exchange in list_of_exchanges:
        coins_list = set()
        #if exchange.name == 'Cryptopia' or exchange.name == 'Bittrex' or exchange.name == 'Kucoin' or exchange.name == 'Huobi Pro':
            #continue #exchange.name == 'Binance' or 
        markets = exchange.fetchMarkets()
        print(markets[0])
        for row in markets:
            #row.base,row.quote,row.symbol,row.type,row.active
            #print(row.keys())
            tuple_data = (exchange.name,row['base'],row['quote'],row['symbol'],row['active'])
            list_of_tuples.append(tuple_data)
            
    return list_of_tuples

setupExchanges(list_of_exchanges)
#print()