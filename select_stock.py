

def select(symbol,start_date,end_date):
    import csv
    import pandas

    df = pandas.read_csv('convert_csv.csv')
    y = df[(df["symbol"] == str(symbol))]
    m = (y['date'] > str(start_date)) & (y['date'] <= str(end_date))
    x = y.loc[m]
    close = x["close"]
    open = x["open"]
    date = x["date"]
    symbol = x["symbol"]
    high = x["high"]
    low = x["low"]
    header = ["open", "high", "low", "close","date"]
    x.to_csv('output.csv', columns = header)






