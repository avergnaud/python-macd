from classes.bittrex_client import get_macd_ohlc
from classes.mongo_client import insert_or_update
from classes.macd_helper import set_ema12

liste_macd = ("USDT-BTC","day")

for macd in liste_macd:
    insert_or_update(macd)

set_ema12()