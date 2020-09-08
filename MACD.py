#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:11:07 2020

@author: no_one
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_MACD(df):
    macd_df = df.copy()
    macd_df['MA_Fast'] = macd_df['Adj Close'].ewm(span = 12 , min_periods = 12).mean()
    macd_df['MA_Slow'] = macd_df['Adj Close'].ewm(span = 26 , min_periods = 26).mean()
    macd_df['MACD'] = macd_df['MA_Fast'] - macd_df['MA_Slow']
    macd_df['Signal'] = macd_df['MACD'].ewm(span = 9 , min_periods = 9).mean()
    return macd_df

currencys = ['BTC-USD','LTC-USD', 'DASH-USD', 'ZEC-USD']
ohlcv_data = {}

for tick in currencys: 
    ohlcv_data[tick] = yf.download(tick, period = '1d', interval = '1m')

BTC_df = get_MACD(ohlcv_data['BTC-USD'])

BTC_df.iloc[:, [4,8,9]].plot(subplots = True, use_index = True, layout = (3,1), title = 'BTC MACD Indicator')
BTC_df.iloc[:, [8,9]].plot()