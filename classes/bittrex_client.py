from bittrex_v2 import Bittrex
from bson.decimal128 import Decimal128

bittrexClient = Bittrex()

def get_macd_ohlc():

    ticks = bittrexClient.get_ticks("USDT-BTC","day")
    liste_macd = []

    for tick in ticks["result"]:

        macd = {
            "exchange":"Bittrex",
            "marketName":"USDT-BTC",
            "tickInterval":"day",
            "open":Decimal128(tick["O"]),
            "high":Decimal128(tick["H"]),
            "low":Decimal128(tick["L"]),
            "close":Decimal128(tick["C"]),
            "volume":Decimal128(tick["V"]),
            "timestamp":tick["T"],
            "ema12": None,
            "ema26": None,
            "macd": None,
            "signal": None
        }
        
        liste_macd.append(macd)

    print("nombre de OHLC récupérés de Bittrex ", len(liste_macd))

    return liste_macd