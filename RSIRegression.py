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

def findPrice():
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

    # Live plots prices
    plt.plot(now, prices, "o")

# for i in range(3):
#     findPrice()
#     time.sleep(1)

# Print prices and now lists (Testing purposes)
# print(prices)
# print(now)

ani = FuncAnimation(plt.gcf(), findPrice(), interval=1000)

# Edits plot of prices over time, between temporary price range of $900 and $1500
plt.xlabel("Time (HH:MM:SS")
plt.ylabel("Price (USD)")
plt.ylim(1050, 1010)
plt.show()
