from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {

}

getPrice = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,DASH&tsyms=BTC,USD,EUR&api_key=1ab438d71f07a76e335c7638ac5c6f3c2d7505ef0bb153496d14819454a7ebc0", params=parameters)
jprint(getPrice.json())
jsonData = json.loads(getPrice.json)
print(jsonData)