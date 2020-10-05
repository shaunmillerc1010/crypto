#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:25:34 2020

@author: no_one

Here we consider the the bollinger bands (20,1) and (20,2) alongside the asking close.
The regression line is given as well.
"""

import numpy as np
import pandas as pd
import datetime
import copy
import matplotlib.pyplot as plt
from indicator_functions_fxcm import *
from scipy.stats import linregress as LinearRegression
from scipy.signal import argrelmin
from scipy.signal import argrelmax
import fxcmpy


# Download historical data for DJI constituent stocks

con = fxcmpy.fxcmpy(config_file='fxcm.cfg')#form connection with account

tickers = ['BTC/USD']
ohlcv_data = {}
for tick in tickers:
    ohlcv_data[tick] = con.get_candles(tick, period='m1', number = 1000)[['bidclose','askclose']]
con.close()

df_bb = get_BB(ohlcv_data['BTC/USD'])
df_bb2 = get_BB(ohlcv_data['BTC/USD'], sigma = 1)
model = LinearRegression([i for i in range(len(ohlcv_data['BTC/USD']))],ohlcv_data['BTC/USD']['askclose'])
dates = [i for i in range(len(df_bb))]
plt.style.use('dark_background')
plt.title('Bollinger Bands for BTC/USD')
plt.fill_between(dates[30:], df_bb["BB_up"][30:], df_bb["BB_dn"][30:], color = 'indigo', label = 'BB sigma = 2')
plt.fill_between(dates[30:], df_bb2["BB_up"][30:], df_bb2["BB_dn"][30:], color = 'darkviolet', label = 'BB sigma = 1')
plt.plot(dates[30:], [model.slope * date + model.intercept for date in dates][30:], color = 'lavenderblush', linewidth = .5, label = 'Regression')
plt.plot(dates[30:],ohlcv_data['BTC/USD']['askclose'][30:], color  = 'fuchsia',linewidth = .5, label = 'Asking Close')
plt.legend(loc = 0)
plt.xticks([0,550,969],[ohlcv_data['BTC/USD'].index[30],ohlcv_data['BTC/USD'].index[610],ohlcv_data['BTC/USD'].index[-1]])
plt.show()
