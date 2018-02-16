import requests
import datetime
import matplotlib.pyplot as plt

x=[0]
y=[0]
fig = plt.gcf()
fig.show()
fig.canvas.draw()
sym=""
i=0


def price(symbol, compare_symbols=['USD']):

    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(compare_symbols).upper())

    page = requests.get(url)
    data = page.json()


    return data

sym=input("Input for bitcoin 'BTC' and for Etherium 'ETH' ")
data = price(sym)


yaxis=1000

for k,v in data.items():
    yaxis= yaxis+int(v);


plt.ylim(0,yaxis)


while(True):


    i+=1
    x.append(i)
    y.append(data['USD'])

    plt.title( sym.upper() +" Vs USD. Last updated at: "+str(datetime.datetime.now()))
    plt.plot(x,y)



    fig.canvas.draw()
    plt.pause(1000)
