from sklearn import linear_model
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

parameters = {
    'exchange': 'binance',
    'interval': '1h',
    'symbol': 'BTC/USDT',
    'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjJjNTEwNjA2YzI4YjU1Y2Q1NmEyMTJiIiwiaWF0IjoxNjU3MDgxOTUyLCJleHAiOjMzMTYxNTQ1OTUyfQ.Jy2RKBIaxY02zRq4MtNeu1Q2-PY8gjmGpUcR6KYK79o'
}

getData = requests.get("https://api.taapi.io/rsi?", params = parameters)
dataJSON = getData.json()
rsi = dataJSON['value']
print(rsi)