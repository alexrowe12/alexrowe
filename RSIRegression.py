from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import time
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    'fsyms': 'ETH',
    'tsyms': 'USD',
    'api_key': '1ab438d71f07a76e335c7638ac5c6f3c2d7505ef0bb153496d14819454a7ebc0'
}

prices = []
now = []

def findPrice(i):
    # Get BTC price from Crypto Compare API, format as integer priceVal in USD
    getPrice = requests.get("https://min-api.cryptocompare.com/data/pricemulti?", params=parameters)
    data = getPrice.json()
    priceUSD = data['ETH']
    priceVal = priceUSD['USD']

    # Get current time, format as HH:MM:SS
    currentTime = datetime.now()
    now.append(currentTime.strftime("%H:%M:%S"))

    # Print time retrieved and price, and append to list prices
    print("Price at " + str(currentTime.strftime("%H:%M:%S")) + ": " + str(priceVal))
    prices.append(priceVal)

    # Finds RSI
    if (len(prices) >= 14):
        totalGain = 0
        totalLoss = 0
        index = len(prices) - 13 + i
        for i in range(14):
            if (i > 1 and i <= 14):
                if (prices[index] >= prices[index - 1]):
                    totalGain += (prices[index] - prices[index - 1])
                elif (prices[index] <= prices[index - 1]):
                    totalLoss += (prices[index - 1] - prices[index])
        avgGain = totalGain / 14
        avgLoss = totalLoss / 14
        RS = avgGain / avgLoss
        RSI = 100 / (1 + RS)
        print("RSI: " + str(RSI))
        # print(totalGain)
        # print(totalLoss)
        # print(avgGain)
        # print(avgLoss)

    # Live plots prices
    plt.cla()
    plt.xlabel("Time (HH:MM:SS")
    plt.ylabel("Price (USD)")
    plt.plot(now, prices, "-")

# Live plots prices using FuncAnimation from matplotlib.animation
ani = FuncAnimation(plt.gcf(), findPrice, interval=1000)
plt.show()

