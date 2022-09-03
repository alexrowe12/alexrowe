from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

cParameters = {
    'fsyms': 'ETH',
    'tsyms': 'USD',
    'api_key': '1ab438d71f07a76e335c7638ac5c6f3c2d7505ef0bb153496d14819454a7ebc0'
}

tParameters = {
    'exchange': 'binance',
    'interval': '1m',
    'symbol': 'BTC/USDT',
    'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjJjNTEwNjA2YzI4YjU1Y2Q1NmEyMTJiIiwiaWF0IjoxNjU3MDgxOTUyLCJleHAiOjMzMTYxNTQ1OTUyfQ.Jy2RKBIaxY02zRq4MtNeu1Q2-PY8gjmGpUcR6KYK79o'
}

prices = []
rsis = []
now = []

def findPrice(i):
    # Get BTC price from Crypto Compare API, format as int priceVal in USD
    getPrice = requests.get("https://min-api.cryptocompare.com/data/pricemulti?", params=cParameters)
    data = getPrice.json()
    priceUSD = data['ETH']
    priceVal = priceUSD['USD']

    # Get BTC RSI from Taapi API, format as int rsi
    getRSI = requests.get("https://api.taapi.io/rsi?", params = tParameters)
    rsiData = getRSI.json()
    rsi = rsiData['value']

    # Get current time, format as HH:MM:SS
    currentTime = datetime.now()
    now.append(currentTime.strftime("%H:%M:%S"))

    # Print time retrieved and price, and append to list prices
    print("Price at " + str(currentTime.strftime("%H:%M:%S")) + ": " + str(priceVal))
    prices.append(priceVal)

    # Print time retrieved and RSI, and append to list rsis
    print("RSI at " + str(currentTime.strftime("%H:%M:%S")) + ": " + str(rsi))
    rsis.append(rsi)

# IDEA: make one graph with RSI vs. Prices vs. Time? or just RSI vs prices? then plot best fit using this data as a predictor

    # if (len(prices) >= 2):
    #     # Reshape to feed into fitter
    #     pricesReshape = np.reshape(prices, (1, -1))
    #     rsisReshape = np.reshape(rsis, (1, -1))

    #     # Finding line of best fit for RSI/Price?
    #     fit_finder = LinearRegression()
    #     fit_finder.fit(pricesReshape, rsisReshape)
    #     best_fit = fit_finder.predict(rsis)

    #     # Output data about best fit line
    #     print(fit_finder.coef_)
    #     print(fit_finder.intercept_)

    # Live plots prices
    plt.figure(0)
    plt.title("Prices vs. Time")
    plt.xlabel("Time (HH:MM:SS)")
    plt.ylabel("Price (USD)")
    plt.plot(now, prices, "-")

    plt.figure(1)
    plt.title("RSI vs. Time")
    plt.xlabel("Time (HH:MM:SS)")
    plt.ylabel("RSI")
    plt.ylim([0, 100])
    plt.plot(now, rsis, "o")

# Live plots prices using FuncAnimation from matplotlib.animation
ani = FuncAnimation(plt.gcf(), findPrice, interval=60000)
plt.figure(0)
plt.show()
plt.figure(1)
plt.show()

