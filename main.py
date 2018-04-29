from bittrex_v2 import Bittrex
from classes.macd import Macd

# macd = Macd(exchange="Bittrex",
#     marketName="USDT-BTC",
#     tickInterval="day",
#     open=9351.00000005,
#     high=9570,
#     low=9205.00000001,
#     close=9300,
#     volume=859.57861887,
#     timestamp="2018-04-29T00:00:00")
# 
# print(macd.close)

bittrexClient = Bittrex()
ticks = bittrexClient.get_ticks("USDT-BTC","day")

liste_macd = []

for tick in ticks["result"]:

    macd = Macd(exchange="Bittrex",
        marketName="USDT-BTC",
        tickInterval="day",
        open=tick["O"],
        high=tick["H"],
        low=tick["L"],
        close=tick["C"],
        volume=tick["V"],
        timestamp=tick["T"])
    
    liste_macd.append(macd)

print("nombre de OHLC récupérés de Bittrex ", len(liste_macd))

print("last signal value ", liste_macd[-1].signal)