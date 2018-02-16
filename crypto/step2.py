
import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt



def GetVal():
    symbol = input(" Type for  Bitcoin 'BTC' and For  Ethereum 'ETH' ")
    dur = input("for minutes 'm' for hour 'h' for day 'd' ")
    limit=0

    if(dur.lower()=="m"):
        dur="histominute"
        limit=9999
    elif(dur.lower()=="h"):
        dur="histohour"
        limit=9999
    elif(dur.lower()=="d"):
        dur="histoday"
        limit=1


    df1 = daily_price_historical(symbol, 'USD',dur,limit)
    plt.plot(df1.timesetamp, df1.close)
    plt.title(symbol.upper() + " To USD")
    plt.ylabel('Price In USD')
    plt.xlabel('Year')
    plt.xticks(rotation=20)
    plt.show()



def daily_price_historical(symbol, comparison_symbol,dur,limit, all_data=True, aggregate=1, exchange=''):


    url = "https://min-api.cryptocompare.com/data/"+dur+"?fsym={}&tsym={}&limit={}&aggregate={}"\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df




GetVal();

