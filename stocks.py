def stocks(stock):
    try:
        import wget
    except:
        import pip
        pip.main(['install', 'wget'])
        import wget
        
    import datetime as dt
    import matplotlib.pyplot as plt 
    from matplotlib import style
    import pandas as pd
    try:
        import pandas_datareader.data as web
    except:
        import pip
        pip.main(['install', 'pandas_datareader'])
        import pandas_datareader.data as web
        
    style.use('ggplot')
    
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)
    
    class Yahoo():
    
        def __init__(self, symbol=None, start=None, end=None):
            import datetime, time
            self.symbol = symbol

            # initialize start/end dates if not provided
            if end is None:
                end = datetime.datetime.today()
            if start is None:
                start = datetime.datetime(2010,1,1)

            self.start = start
            self.end = end

            # convert dates to unix time strings
            unix_start = int(time.mktime(self.start.timetuple()))
            day_end = self.end.replace(hour=23, minute=59, second=59)
            unix_end = int(time.mktime(day_end.timetuple()))

            url = 'https://finance.yahoo.com/quote/{}/history?'
            url += 'period1={}&period2={}'
            url += '&filter=history'
            url += '&interval=1d'
            url += '&frequency=1d'
            self.url = url.format(self.symbol, unix_start, unix_end)
        
    def read(self):
        import requests, re, json
       
        r = requests.get(self.url)
        
        ptrn = r'root\.App\.main = (.*?);\n}\(this\)\);'
        txt = re.search(ptrn, r.text, re.DOTALL).group(1)
        jsn = json.loads(txt)
        df = pd.DataFrame(
                jsn['context']['dispatcher']['stores']
                ['HistoricalPriceStore']['prices']
                )
        df.insert(0, 'symbol', self.symbol)
        df['date'] = pd.to_datetime(df['date'], unit='s').dt.date
        
        # drop rows that aren't prices
        df = df.dropna(subset=['close'])
        
        df = df[['symbol', 'date', 'high', 'low', 'open', 'close', 
                 'volume', 'adjclose']]
        df = df.set_index('symbol')
        return df
    
    ydr = Yahoo(stock)
    df = ydr.read()
        
    print(df.head(6))

    print(df['open'][0:5])
    df.to_csv('symboldf = pd.read_csv("stock.csv").csv')
    df = pd.read_csv('symbolprint(df.head()).csv')
    print(df.head())
    df = pd.read_csv('stock.csv', parse_dates=True, index_col=0)
    
    df.plot()
    plt.show()
    
    df['adjclose'].plot()
    plt.show()
    
    print(df['adjclose'])
    print(df[['open', 'high']].head())