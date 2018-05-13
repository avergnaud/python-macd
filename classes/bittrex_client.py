from bittrex_v2 import Bittrex
from bson.decimal128 import Decimal128

bittrexClient = Bittrex()

# exemples :
# "USDT-BTC"
# “oneMin”, “fiveMin”, “thirtyMin”, “hour”, “day”
def get_macd_ohlc(marketName,tickInterval):

    ticks = bittrexClient.get_ticks(marketName,tickInterval)
    liste_macd = []

    for tick in ticks["result"]:

        macd = {
            "exchange":"Bittrex",
            "marketName":marketName,
            "tickInterval":tickInterval,
            #"open":Decimal128(tick["O"]),
            #"high":Decimal128(tick["H"]),
            #"low":Decimal128(tick["L"]),
            #"close":Decimal128(tick["C"]),
            #"volume":Decimal128(tick["V"]),
            "open":float(tick["O"]),
            "high":float(tick["H"]),
            "low":float(tick["L"]),
            "close":float(tick["C"]),
            "volume":float(tick["V"]),
            "timestamp":tick["T"],
            "ema12": None,
            "ema26": None,
            "macd": None,
            "signal": None
        }
        
        liste_macd.append(macd)

    print("nombre de OHLC récupérés de Bittrex ", len(liste_macd))

    # à valider :
    return liste_macd[-1000:]