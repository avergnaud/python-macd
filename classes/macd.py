class Macd:
    
    def __init__(self, exchange, marketName, tickInterval, open, high, low, close, volume, timestamp):
        self.exchange = exchange
        self.marketName = marketName
        self.tickInterval = tickInterval
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.timestamp = timestamp
        # attributs qui seront valorisés après l'instanciation :
        self.ema12 = None
        self.ema26 = None
        self.macd = None
        self.signal = None

    def __repr__(self):
        return repr((self.exchange, self.marketName, self.tickInterval, self.timestamp))