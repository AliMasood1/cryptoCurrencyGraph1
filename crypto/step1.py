import requests


def price(symbol, compare_symbols=['USD']):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(compare_symbols).upper())

    page = requests.get(url)
    data = page.json()
    return data

ans = input(" Type for  Bitcoin 'BTC' and For  Ethereum 'ETH' ")
print("The current price of " +ans+ " in USD=", price(ans.upper()))