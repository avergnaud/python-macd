from classes.mongo_client import get_all, update_one
import numpy
from bson.decimal128 import Decimal128

def set_ema12():
    i=0
    macds = get_all()

    first_twelve_macd = macds[:12]

    for macd in macds:
        i += 1
        if macd["ema12"] is not None:
            continue
        
        if i==12:
            first_twelve_closing = []
            for fmacd in first_twelve_macd:
                first_twelve_closing.append(fmacd["close"].to_decimal())
            average = numpy.mean(first_twelve_closing)
            macd["ema12"] = Decimal128(average)
            update_one(macd)