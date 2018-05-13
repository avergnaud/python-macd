import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
from mpl_finance import candlestick_ohlc
from classes.bittrex_client import get_macd_ohlc

quotes = pd.DataFrame(get_macd_ohlc("USDT-BTC","day"))

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

# https://stackoverflow.com/questions/46737330/typeerror-strptime-argument-1-must-be-string-not-series

quotes['timestamp_datetime'] = [datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S") for x in quotes['timestamp'] ] 

date1 = datetime.datetime.strptime("2017-12-15T00:00:00", "%Y-%m-%dT%H:%M:%S")
quotes = quotes[(quotes['timestamp_datetime'] >= date1)]

candlestick_ohlc(ax, zip(mdates.date2num(quotes['timestamp_datetime']),
                         quotes['open'], quotes['high'],
                         quotes['low'], quotes['close']),
                 width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()