#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:24:04 2020

@author: no_one

ALL algorithmic functions
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as LinearRegression
from scipy.signal import argrelmin
from scipy.signal import argrelmax


def get_BB(df,n = 20, sigma = 2):
    "Calculate Bollinger Band"
    bb_df = df.copy()
    bb_df["MA"] = bb_df['askclose'].rolling(n).mean()
    bb_df["BB_up"] = bb_df["MA"] + sigma*bb_df['askclose'].rolling(n).std(ddof=0) #ddof=0 is required since we want to take the standard deviation of the population and not sample
    bb_df["BB_dn"] = bb_df["MA"] - sigma*bb_df['askclose'].rolling(n).std(ddof=0) #ddof=0 is required since we want to take the standard deviation of the population and not sample
    bb_df["BB_width"] = bb_df["BB_up"] - bb_df["BB_dn"]
    bb_df.fillna(value = bb_df['askclose'][0], inplace=True)
    return bb_df

def buy_to_amount(adj_close, to_amount):
    '''returns number of shares needed to meet amount and total cost'''
    shares = int(to_amount//adj_close)
    return shares, adj_close * shares
